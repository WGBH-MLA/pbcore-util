from jsonschema_rs import validator_for, ValidationError
from json import load
from pytest import fixture, raises, mark


@fixture
def validator(schema_path='schemas/pbcore.schema.json'):
    with open(schema_path, 'r') as schema_file:
        schema = load(schema_file)

    return validator_for(schema).validate


@fixture
def mvp():
    return {
        "pbcoreDescriptionDocument": {
            "xsi:schemaLocation": "http://www.example.com/schema",
            "pbcoreIdentifier": [{"text": "123", "source": "example"}],
            "pbcoreTitle": [{"text": "Title"}],
            "pbcoreDescription": [{"text": ""}],
        },
    }


def test_mvpbcore(validator, mvp):
    """Test minimum viable pbcore document. This should pass."""
    validator(mvp)


def test_pbcore_schema_is_valid_schema(validator):
    from types import BuiltinFunctionType

    assert validator is not None
    assert isinstance(validator, BuiltinFunctionType)


def test_pbcore_empty_document(validator):
    """Test empty document. This should fail."""
    with raises(ValidationError) as error:
        validator({})
    assert error.value.message == '"pbcoreDescriptionDocument" is a required property'


def test_pbcoreDescriptionDocument_invalid_types(validator):
    """Test pbcoreDescriptionDocument invalid types."""
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": "Test description"})
    assert error.value.message == '"Test description" is not of type "object"'
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": 3})
    assert error.value.message == '3 is not of type "object"'
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": 3.14})
    assert error.value.message == '3.14 is not of type "object"'
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": []})
    assert error.value.message == '[] is not of type "object"'
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": None})
    assert error.value.message == 'null is not of type "object"'


def test_xsi_schemaLocation_missing(validator):
    """Test document with an empty description object. This should fail."""
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": {}})
    assert error.value.message == '"xsi:schemaLocation" is a required property'


def test_pbcoreIdentifier_missing(validator):
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


def test_pbcoreIdentifier_missing_data(validator):
    """Test document with an empty identifier. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [],
                }
            }
        )
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreIdentifier_missing_text(validator):
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


def test_pbcoreIdentifier_missing_source(validator):
    """Test document with an empty identifier source. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123"}],
                },
            }
        )
    assert error.value.message == '"source" is a required property'


def test_pbcoreIdentifier_invalid(validator):

    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [
                        {
                            "text": "123",
                            "source": "somewhere",
                            "extra_value": "not allowed",
                        }
                    ],
                },
            }
        )
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )


def test_pbcoreTitle_missing(validator):
    """Test document without a pbcoreTitle. This should fail."""
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


def test_pbcoreTitle_missing_data(validator):
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                    "pbcoreTitle": [],
                },
            }
        )
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreTitle_missing_text(validator):
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                    "pbcoreTitle": [{"source": "Test Source"}],
                },
            }
        )
    assert error.value.message == '"text" is a required property'


def test_pbcoreTitle_invalid(validator):
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                    "pbcoreTitle": [
                        {"text": "Test Title", "extra_value": "not allowed"}
                    ],
                },
            }
        )
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )


def test_pbcoreDescription_missing(validator):
    """Test document with an empty description. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                    "pbcoreTitle": [{"text": "Title"}],
                },
            }
        )
    assert error.value.message == '"pbcoreDescription" is a required property'


def test_pbcoreDescription_empty(validator):
    """Test document with an empty description. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                    "pbcoreTitle": [{"text": "Title"}],
                    "pbcoreDescription": [],
                },
            }
        )
    assert error.value.message == '[] has less than 1 item'


@mark.xfail
def test_pbcoreDescription_invalid(validator):
    """Test document with an invalid description. This should fail."""
    with raises(ValidationError) as error:
        validator(
            {
                "pbcoreDescriptionDocument": {
                    "xsi:schemaLocation": "http://www.example.com/schema",
                    "pbcoreIdentifier": [{"text": "123", "source": "example"}],
                    "pbcoreTitle": [{"text": "Title"}],
                    "pbcoreDescription": [
                        {"text": "Description", "extra_value": "property"}
                    ],
                },
            }
        )
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )
