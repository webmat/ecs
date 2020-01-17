from generators import ecs_helpers


def generate(ecs_nested, ecs_flat, normalized):
    ecs_helpers.yaml_dump('generated/ecs/ecs_flat.yml', ecs_flat)
    ecs_helpers.yaml_dump('generated/ecs/ecs_nested.yml', ecs_nested)
    ecs_helpers.yaml_dump('generated/ecs/normalized_fields.yml', normalized)
