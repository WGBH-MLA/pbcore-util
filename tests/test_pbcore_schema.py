from jsonschema_rs import validator_for, ValidationError
from json import load
from pytest import fixture, raises


@fixture
def validator(schema_path='schemas/pbcore.schema.json'):
    with open(schema_path, 'r') as schema_file:
        schema = load(schema_file)

    return validator_for(schema).validate


def test_pbcore_schema_is_valid_schema(validator):
    from types import BuiltinFunctionType

    assert validator is not None
    assert isinstance(validator, BuiltinFunctionType)


def test_pbcore_empty_document(validator):
    """Test empty document. This should fail."""
    with raises(ValidationError) as error:
        validator({})
    assert error.value.message == '"pbcoreDescriptionDocument" is a required property'


def test_description_only(validator):
    """Test document with description only. This should fail."""
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": "Test description"})
    assert error.value.message == '"Test description" is not of type "object"'


def test_missing_xsi_schemaLocation(validator):
    """Test document with an empty description object. This should fail."""
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": {}})
    assert error.value.message == '"xsi:schemaLocation" is a required property'


def test_missing_pbcoreIdentifier(validator):
    """Test document with an empty identifier. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema"
                }
            }
        )
    assert error.value.message == '"pbcoreIdentifier" is a required property'


def test_missing_pbcoreIdentifierText(validator):
    """Test document with an empty identifier text. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"source": "example"}],
                },
            }
        )
    assert error.value.message == '"text" is a required property'


def test_missing_pbcoreIdentifierSource(validator):
    """Test document with an empty identifier source. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "example"}],
                },
            }
        )
    assert error.value.message == '"source" is a required property'


def test_missing_pbcoreTitle(validator):
    """Test document with an empty title. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                },
            }
        )
    assert error.value.message == '"pbcoreTitle" is a required property'
