from pbcore import PBCore


def regenerate_schema(schema_path: str = "schemas/pbcore.schema.json"):
    """Regenerate the PBCore JSON schema from the Pyeantic models and save it to
    the specified path."""
    schema = PBCore.model_json_schema()
    with open(schema_path, "w") as schema_file:
        import json

        json.dump(schema, schema_file, indent=2)
