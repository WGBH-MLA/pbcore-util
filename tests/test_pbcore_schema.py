# from jsonschema_rs import ValidationError
from pydantic import ValidationError
from pytest import raises, mark
from pbcore import PBCore

invalid_element_types = [
    3,
    3.14,
    None,
    [],
    "",
]
invalid_text_elements = [
    {},
    {"text": 3},
    {"text": 3.14},
    {"text": None},
    {"text": {}},
    {"text": []},
    # {"text": "v"},
]

# def check_invalid_text_elements(element, ):


def test_mvpbcore(mvp):
    """Test minimum viable pbcore document. This should pass."""
    pbcore = PBCore(**mvp)


def test_pbcore_empty_document():
    """Test empty document. This should fail."""
    with raises(ValidationError) as error:
        PBCore()
    assert 'pbcoreDescriptionDocument' in str(error.value)
    assert 'Field required [type=missing, input_value={}, input_type=dict]' in str(
        error.value
    )


def test_invalid_pbcoreDescriptionDocument_types():
    """Test invalid types."""

    for bad_value in invalid_element_types:
        with raises(ValidationError) as error:
            PBCore(pbcoreDescriptionDocument=bad_value)
        assert (
            f'''Input should be a valid dictionary or instance of PBCoreDescriptionDocument [type=model_type, input_value={bad_value if bad_value is not "" else "''"}, input_type={type(bad_value).__name__}]'''
            in str(error.value)
        )


def test_invalid_pbcoreDescriptionDocument_elements():
    for bad_value in invalid_text_elements:
        with raises(ValidationError) as error:
            PBCore(pbcoreDescriptionDocument=bad_value)
        assert '4 validation errors for PBCore' in str(error.value)
        # assert (
        #     "Field required [type=missing, input_value={'pbcoreTitle': [{}]}, input_type=dict]"
        #     in str(error.value)
        # )


def test_xsi_schemaLocation_missing(validator):
    """Test document with an empty description object. This should fail."""
    with raises(ValidationError) as error:
        validator({"pbcoreDescriptionDocument": {}})
    assert error.value.message == '"xsi:schemaLocation" is a required property'


def test_pbcoreIdentifier_missing(validator, mvp):
    """Test document with an empty identifier. This should fail."""
    del mvp['pbcoreDescriptionDocument']['pbcoreIdentifier']
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"pbcoreIdentifier" is a required property'


def test_pbcoreIdentifier_missing_data(validator, mvp):
    """Test document with an empty identifier. This should fail."""
    mvp['pbcoreDescriptionDocument']['pbcoreIdentifier'] = []
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreIdentifier_missing_text(validator, mvp):
    """Test document with an empty identifier text. This should fail."""
    del mvp['pbcoreDescriptionDocument']['pbcoreIdentifier'][0]['text']
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"text" is a required property'


def test_pbcoreIdentifier_missing_source(validator, mvp):
    """Test document with an empty identifier source. This should fail."""
    del mvp['pbcoreDescriptionDocument']['pbcoreIdentifier'][0]['source']
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"source" is a required property'


def test_pbcoreIdentifier_invalid(validator, mvp):
    mvp['pbcoreDescriptionDocument']['pbcoreIdentifier'][0][
        'extra_value'
    ] = "not allowed"
    with raises(ValidationError) as error:
        validator(mvp)
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )


def test_pbcoreIdentifier_multiple(validator, mvp):
    """Test document with multiple pbcoreIdentifier elements."""
    mvp['pbcoreDescriptionDocument']['pbcoreIdentifier'].append(
        {
            "text": "video-2",
            "source": "local",
        }
    )
    validator(mvp)


def test_pbcoreTitle_missing(validator, mvp):
    """Test document without a pbcoreTitle. This should fail."""
    del mvp['pbcoreDescriptionDocument']['pbcoreTitle']
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"pbcoreTitle" is a required property'


def test_pbcoreTitle_missing_data(validator, mvp):
    """Test document with an empty title. This should fail."""
    mvp['pbcoreDescriptionDocument']['pbcoreTitle'] = []
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreTitle_missing_text(validator, mvp):
    """Test document with a missing title text. This should fail."""
    del mvp['pbcoreDescriptionDocument']['pbcoreTitle'][0]['text']
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"text" is a required property'


def test_pbcoreTitle_invalid(validator, mvp):
    """Test pbcore with invalid title attributes."""
    mvp['pbcoreDescriptionDocument']['pbcoreTitle'][0]['extra_value'] = "not allowed"
    with raises(ValidationError) as error:
        validator(mvp)
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )
    mvp['pbcoreDescriptionDocument']['pbcoreTitle'][0]


def test_pbcoreTitle_multiple(validator, mvp):
    """Test document with multiple pbcoreTitle elements."""
    mvp['pbcoreDescriptionDocument']['pbcoreTitle'].append({"text": "Alternate title"})
    validator(mvp)


def test_pbcoreDescription_missing(validator, mvp):
    """Test document with an empty description. This should fail."""
    del mvp['pbcoreDescriptionDocument']['pbcoreDescription']
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"pbcoreDescription" is a required property'


def test_pbcoreDescription_empty(validator, mvp):
    """Test document with an empty description. This should fail."""
    mvp['pbcoreDescriptionDocument']['pbcoreDescription'] = []
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreDescription_multiple(validator, mvp):
    """Test document with multiple pbcoreDescription elements."""
    mvp['pbcoreDescriptionDocument']['pbcoreDescription'].append(
        {"text": "Alternate description"}
    )
    validator(mvp)


@mark.xfail
def test_pbcoreDescription_invalid(validator, mvp):
    """Test document with an invalid description. This should fail."""
    mvp['pbcoreDescriptionDocument']['pbcoreDescription'][0][
        'extra_value'
    ] = "not allowed"
    with raises(ValidationError) as error:
        validator(mvp)
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )
