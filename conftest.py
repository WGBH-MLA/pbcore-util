from jsonschema_rs import validator_for
from json import load
from pytest import fixture

from pbcore.models.models import PBCore


@fixture
def validator(schema_path='schemas/pbcore.schema.json', scope='module'):
    """Return a rust-compiled PBCore schema validator."""
    with open(schema_path, 'r') as schema_file:
        schema = load(schema_file)

    # return validator_for(schema).validate
    return PBCore.model_validate


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


@fixture
def pbcore(mvp, scope='module'):
    """Return a PBCore model."""

    return PBCore(**mvp)
