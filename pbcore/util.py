from pbcore import PBCore


def regenerate_schema(schema_path="schemas/pbcore.schema.json"):
    """Regenerate the PBCore JSON schema and save it to the specified path."""
    schema = PBCore.model_json_schema()
    with open(schema_path, "w") as schema_file:
        import json

        json.dump(schema, schema_file, indent=2)
