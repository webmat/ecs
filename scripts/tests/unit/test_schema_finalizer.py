import os
import pprint
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from schema import finalizer

class TestSchemaFinalizer(unittest.TestCase):


    def setUp(self):
        self.maxDiff = None


    def schema_base(self):
        return {
            'base': {
                'schema_details': {
                    'title': 'Base',
                    'root': True,
                },
                'field_details': {
                    'name': 'base',
                },
                'fields': {
                    '@timestamp': {
                        'field_details': {
                            'name': '@timestamp',
                        }
                    },
                }
            }
        }


    def schema_process(self):
        return {
            'process': {
                'schema_details': {
                    'title': 'Process',
                    'root': False,
                    'reusable':{
                        'top_level': True,
                        'expected': [
                            {'full': 'process.parent', 'at': 'process', 'as': 'parent'},
                        ]
                    }
                },
                'field_details': {
                    'name': 'process',
                },
                'fields': {
                    'pid': {
                        'field_details': {
                            'name': 'pid',
                        }
                    },
                    'thread': {
                        'field_details': {'name': 'thread'},
                        'fields': {
                            'id': {
                                'field_details': {'name': 'thread.id'}
                            }
                        }
                    }
                }
            }
        }


    def schema_user(self):
        return {
            'user': {
                'schema_details': {
                    'root': False,
                    'reusable':{
                        'top_level': True,
                        'expected': [
                            {'full': 'server.user', 'at': 'server', 'as': 'user'},
                            {'full': 'user.target', 'at': 'user', 'as': 'target'},
                            {'full': 'user.effective', 'at': 'user', 'as': 'effective'},
                        ]
                    }
                },
                'field_details': {
                    'name': 'user',
                    'type': 'group',
                },
                'fields': {
                    'name': {
                        'field_details': {
                            'name': 'name',
                        }
                    }
                }
            }
        }


    def schema_server(self):
        return {
            'server': {
                'schema_details': {'root': False},
                'field_details': {
                    'name': 'server',
                    'type': 'group'
                },
                'fields': {
                    'ip': {
                        'field_details': {
                            'name': 'ip',
                            'type': 'ip'
                        }
                    }
                }
            }
        }

    # perform_reuse


    def test_perform_reuse_with_foreign_reuse_and_self_reuse(self):
        fields = {**self.schema_user(), **self.schema_server(), **self.schema_process()}
        # If the test had multiple foreign destinations for user fields, we could compare them together instead
        original_user_fields_identity = id(fields['user']['fields'])
        finalizer.perform_reuse(fields)
        process_fields = fields['process']['fields']
        server_fields = fields['server']['fields']
        user_fields = fields['user']['fields']
        # Expected reuse
        self.assertIn('parent', process_fields)
        self.assertIn('user', server_fields)
        self.assertIn('target', user_fields)
        self.assertIn('effective', user_fields)
        # Only foreign reuse copies fields by reference
        self.assertTrue(server_fields['user']['referenced_fields'])
        self.assertEqual(id(server_fields['user']['fields']), original_user_fields_identity)
        self.assertNotIn('referenced_fields', user_fields['target'])
        # Leaf field sanity checks for reuse
        self.assertIn('name', user_fields['target']['fields'])
        self.assertIn('name', user_fields['effective']['fields'])
        self.assertIn('name', server_fields['user']['fields'])
        self.assertIn('pid', process_fields['parent']['fields'])
        # No unexpected cross-nesting
        self.assertNotIn('target', user_fields['target']['fields'])
        self.assertNotIn('target', user_fields['effective']['fields'])
        self.assertNotIn('target', server_fields['user']['fields'])
        # Legacy nestings at host schema level
        self.assertIn('process.parent', fields['process']['schema_details']['nestings'])
        self.assertIn('user.effective', fields['user']['schema_details']['nestings'])
        self.assertIn('user.target', fields['user']['schema_details']['nestings'])
        self.assertIn('server.user', fields['server']['schema_details']['nestings'])
        # New nested_here at host schema level
        self.assertIn({'full':'process.parent','schema_name':'process'},
                fields['process']['schema_details']['reused_here'])
        self.assertIn({'full':'user.effective','schema_name':'user'},
                fields['user']['schema_details']['reused_here'])
        self.assertIn({'full':'user.target','schema_name':'user'},
                fields['user']['schema_details']['reused_here'])
        self.assertIn({'full':'server.user','schema_name':'user'},
                fields['server']['schema_details']['reused_here'])
        # Reused fields have an indication they're reused
        self.assertEqual(process_fields['parent']['field_details']['original_fieldset'], 'process',
                "The parent field of reused fields should have 'original_fieldset' populated")
        self.assertEqual(process_fields['parent']['fields']['pid']['field_details']['original_fieldset'], 'process',
                "Leaf fields of reused fields for self-nested fields should have 'original_fieldset' populated already")
        self.assertEqual(server_fields['user']['field_details']['original_fieldset'], 'user',
                "The parent field of reused fields should have 'original_fieldset' populated")
        # Not calculated yet because foreign nestings are by reference
        # self.assertEqual(server_fields['user']['fields']['name']['field_details']['original_fieldset'], 'user')

    # calculate_final_values


    def test_calculate_final_values_makes_nested_fields_fully_independent(self):
        fields = {**self.schema_base(), **self.schema_user(), **self.schema_server()}
        original_user_fields_identity = id(fields['user']['fields'])
        finalizer.perform_reuse(fields)
        finalizer.calculate_final_values(fields)
        base_fields = fields['base']['fields']
        server_fields = fields['server']['fields']
        user_fields = fields['user']['fields']
        # References are all resolved, original_fieldset is set everywhere
        self.assertNotEqual(id(server_fields['user']['fields']), original_user_fields_identity,
                "Foreign reused fields should no longer be by reference")
        self.assertNotIn('referenced_fields', server_fields['user'],
                "The 'referenced_fields' attribute should have been removed")
        self.assertEqual(server_fields['user']['fields']['name']['field_details']['original_fieldset'], 'user',
                "original_fieldset should be populated in the independent copy of the reused fields")
        # Pre-calculated path-based values
        # root=true
        timestamp_details = base_fields['@timestamp']['field_details']
        self.assertEqual(timestamp_details['flat_name'], '@timestamp',
            "Field sets with root=true must not namespace field names with the field set's name")
        self.assertEqual(timestamp_details['dashed_name'], '@timestamp')
        # root=false
        self.assertEqual(server_fields['ip']['field_details']['flat_name'], 'server.ip',
            "Field sets with root=false must namespace field names with the field set's name")
        self.assertEqual(server_fields['ip']['field_details']['dashed_name'], 'server-ip')
        # reused
        server_user_name_details = server_fields['user']['fields']['name']['field_details']
        self.assertEqual(server_user_name_details['flat_name'], 'server.user.name')
        self.assertEqual(server_user_name_details['dashed_name'], 'server-user-name')
        # self-nestings
        user_target_name_details = user_fields['target']['fields']['name']['field_details']
        self.assertEqual(user_target_name_details['flat_name'], 'user.target.name')
        self.assertEqual(user_target_name_details['dashed_name'], 'user-target-name')



    # field_group_at_path


    def test_field_group_at_path_root_destination(self):
        all_fields = self.schema_server()
        fields = finalizer.field_group_at_path('server', all_fields)
        self.assertIn('ip', fields.keys(),
                "should return the dictionary of server fields")


    def test_field_group_at_path_find_nested_destination(self):
        all_fields = self.schema_process()
        fields = finalizer.field_group_at_path('process.thread', all_fields)
        self.assertIn('id', fields.keys(),
                "should return the dictionary of process.thread fields")
        self.assertEqual('thread.id', fields['id']['field_details']['name'])


    def test_field_group_at_path_missing_nested_path(self):
        all_fields = self.schema_server()
        with self.assertRaisesRegex(ValueError, "Field server.nonexistent not found"):
            finalizer.field_group_at_path('server.nonexistent', all_fields)


    def test_field_group_at_path_leaf_field_not_field_group(self):
        all_fields = self.schema_server()
        with self.assertRaisesRegex(ValueError, "Field server\.ip \(type ip\) already exists"):
            finalizer.field_group_at_path('server.ip', all_fields)


    def test_field_group_at_path_for_leaf_object_field_creates_the_section(self):
        all_fields = {
            'network': {
                'field_details': {
                    'name': 'network',
                },
                'fields': {
                    'ingress': {
                        'field_details': {
                            'name': 'network.ingress',
                            'type': 'object'
                        }
                    }
                }
            }
        }
        ingress_subfields = finalizer.field_group_at_path('network.ingress', all_fields)
        self.assertEqual(ingress_subfields, {})
        self.assertEqual(all_fields['network']['fields']['ingress']['fields'], {})
