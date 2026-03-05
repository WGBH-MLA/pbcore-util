import json
from pydantic import ValidationError
from pytest import raises, mark
from pbcore import PBCore
from tests.helpers import (
    assert_validation_error,
    list_fields_optional,
    list_fields_required,
    pbcore_element_models,
)
from tests import pbcore_test_data as td


def test_schema_unchanged():
    generated = PBCore.model_json_schema()
    with open("schemas/pbcore.schema.json") as f:
        stored = json.load(f)

    assert generated == stored


@mark.parametrize("list_field", list_fields_optional())
def test_list_fields_optional(list_field):
    """Optional list fields may be None (empty list will still raise error)."""
    data = td.pbcoreDescriptionDocument()
    data[list_field] = None
    assert isinstance(PBCore(pbcoreDescriptionDocument=data), PBCore)


@mark.parametrize("list_field", list_fields_required())
def test_list_fields_with_invalid_empty(list_field):
    """Raise error if required list field is empty."""
    data = td.pbcoreDescriptionDocument()
    data[list_field] = []

    with raises(ValidationError) as error:
        PBCore(pbcoreDescriptionDocument=data)

    assert_validation_error(
        error.value,
        expected_errors=[
            {"loc": ("pbcoreDescriptionDocument", list_field), "type": "too_short"}
        ],
    )


@mark.parametrize("list_field", list_fields_required())
def test_list_fields_with_invalid_value(list_field):
    """Raise error if required list field is empty."""
    data = td.pbcoreDescriptionDocument()
    data[list_field] = "i ain't no list!"

    with raises(ValidationError) as error:
        PBCore(pbcoreDescriptionDocument=data)

    assert_validation_error(
        error.value,
        expected_errors=[
            {"loc": ("pbcoreDescriptionDocument", list_field), "type": "list_type"}
        ],
    )


@mark.parametrize("list_field", list_fields_required())
def test_list_fields_required_missing(list_field):
    """Raise error if required list field is missing."""
    data = td.pbcoreDescriptionDocument()
    data.pop(list_field, None)

    with raises(ValidationError) as error:
        PBCore(pbcoreDescriptionDocument=data)

    assert_validation_error(
        error.value,
        expected_errors=[
            {"loc": ("pbcoreDescriptionDocument", list_field), "type": "missing"}
        ],
    )


@mark.parametrize("model", pbcore_element_models())
def test_pbcore_element_valid(model_factory, model, ids=lambda m: m.__name__):
    """
    Test happy PBCore model validation using a model factory and test data.
    """
    # This will raise an error if validation fails.
    valid_instance = model_factory(model)
    assert isinstance(valid_instance, model)
