import sys


def generate(ecs_nested, ecs_version):
    save_asciidoc('docs/fields.asciidoc', render_field_index(ecs_nested))
    save_asciidoc('docs/field-details.asciidoc', render_field_details(ecs_nested))

# Helpers


def sorted_by_keys(dict, sort_keys):
    if not isinstance(sort_keys, list):
        sort_keys = [sort_keys]
    tuples = []
    for key in dict:
        nested = dict[key]

        sort_criteria = []
        for sort_key in sort_keys:
            sort_criteria.append(nested[sort_key])
        sort_criteria.append(nested)
        tuples.append(sort_criteria)

    return list(map(lambda t: t[-1], sorted(tuples)))


# Rendering

# Field Index


def render_field_index(ecs_nested):
    page_text = index_header()
    for fieldset in sorted_by_keys(ecs_nested, ['group', 'name']):
        page_text += render_index_row(fieldset)
    page_text += table_footer()
    page_text += index_footer()
    return page_text


def render_index_row(fieldset):
    return index_row().format(
        fieldset_id='ecs-' + fieldset['name'],
        fieldset_title=fieldset['title'],
        fieldset_short=fieldset.get('short', fieldset['description'])
    )


# Field Details

def render_field_details(ecs_nested):
    page_text = ''
    for fieldset in sorted_by_keys(ecs_nested, ['group', 'name']):
        page_text += render_fieldset(fieldset)
    return page_text


def render_fieldset(fieldset):
    fieldset_text = fieldset_header().format(
        fieldset_id='ecs-' + fieldset['name'],
        fieldset_description=fieldset['description'],
        fieldset_title=fieldset['title']
    )
    for field_name in sorted(fieldset['fields']):
        fieldset_text += render_field(fieldset['fields'][field_name])
    fieldset_text += table_footer()
    return fieldset_text


def render_field(field):
    example = ''
    if 'example' in field:
        example = 'example: ' + str(field['example'])
    field_text = field_row().format(
        field_name=field['flat_name'],
        field_short=field['short'],
        field_example=example,
        field_level=field['level'],
        field_type=field['type'],
    )
    return field_text

# Templates


def table_footer():
    return '''
|=====
'''


# Field Index


def index_header():
    return '''
[[ecs-fields]]
== {ecs} Fields

[float]
[[ecs-fieldsets]]
=== Field Sets
[cols="<,<",options="header",]
|=======================================================================
| Field Set  | Description
'''


def index_row():
    return '''
| <<{fieldset_id},{fieldset_title}>> | {fieldset_short}
'''


def index_footer():
    return '''
include::field-details.asciidoc[]
'''


# Field Details


def fieldset_header():
    return '''
[[{fieldset_id}]]
=== {fieldset_title} fields

{fieldset_description}

[options="header"]
|=====
| Field  | Description  | Level / Type

// ===============================================================
'''


def field_row():
    return '''
| {field_name}
| {field_short}

{field_example}

| level: {field_level}

type: {field_type}

// ===============================================================
'''

# File


def save_asciidoc(file, text):
    open_mode = "wb"
    if sys.version_info >= (3, 0):
        open_mode = "w"
    with open(file, open_mode) as outfile:
        outfile.write(text)
