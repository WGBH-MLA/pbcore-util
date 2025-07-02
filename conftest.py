from jsonschema_rs import validator_for, ValidationError
from json import load
from pytest import fixture, raises, mark


@fixture
def validator(schema_path='schemas/pbcore.schema.json', scope='module'):
    with open(schema_path, 'r') as schema_file:
        schema = load(schema_file)

    return validator_for(schema).validate


@fixture
def mvp(scope='module'):
    """Return a minimum viable pbcore document."""
    return {
        "pbcoreDescriptionDocument": {
            "xsi:schemaLocation": "http://www.example.com/schema",
            "pbcoreIdentifier": [{"text": "123", "source": "example"}],
            "pbcoreTitle": [{"text": "Title"}],
            "pbcoreDescription": [{"text": ""}],
        },
    }
