import yaml
from collections import OrderedDict


def generate(ecs_nested, ecs_version):
    # base first
    beats_fields = fieldset_field_array(ecs_nested['base']['fields'])

    allowed_fieldset_keys = ['name', 'title', 'group', 'description', 'footnote', 'type']
    # other fieldsets
    for fieldset_name in sorted(ecs_nested):
        if 'base' == fieldset_name:
            continue
        fieldset = ecs_nested[fieldset_name]

        beats_field = dict_copy_keys_ordered(fieldset, allowed_fieldset_keys)
        beats_field['fields'] = fieldset_field_array(fieldset['fields'])
        beats_fields.append(beats_field)

    beats_file = OrderedDict()
    beats_file['key'] = 'ecs'
    beats_file['title'] = 'ECS'
    beats_file['description'] = 'ECS Fields.'
    beats_file['fields'] = beats_fields

    write_beats_yaml(beats_file, ecs_version)


def fieldset_field_array(source_fields):
    allowed_keys = ['name', 'level', 'required', 'type', 'object_type',
                    'ignore_above', 'multi_fields', 'format',
                    'description', 'example']
    fields = []
    for nested_field_name in source_fields:
        ecs_field = source_fields[nested_field_name]
        beats_field = dict_copy_keys_ordered(ecs_field, allowed_keys)
        beats_field['name'] = nested_field_name
        fields.append(beats_field)
    return fields

# Helpers


def write_beats_yaml(beats_file, ecs_version):

    with open('generated/beats/fields.ecs.yml', 'w') as outfile:
        outfile.write(file_header().format(version=ecs_version))
        yaml.dump([beats_file], outfile, default_flow_style=False)


def dict_copy_keys_ordered(dict, copied_keys):
    ordered_dict = OrderedDict()
    for key in copied_keys:
        if key in dict:
            ordered_dict[key] = dict[key]
    return ordered_dict


def indent(text, indent, char=' '):
    padding = indent * char
    return ''.join(padding + line for line in text.splitlines(True))

# Rendering


def yaml_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


yaml.add_representer(OrderedDict, yaml_ordereddict)

# Templates


def file_header():
    return '''
# WARNING! Do not edit this file directly, it was generated by the ECS project,
# based on ECS version {version}.
# Please visit https://github.com/elastic/ecs to suggest changes to ECS fields.

'''.lstrip()
