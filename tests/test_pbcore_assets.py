from jsonschema_rs import ValidationError
from pytest import raises


def test_pbcoreAssetType(validator, mvp):
    """Test pbcoreAssetType."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = [{"text": "video"}]
    validator(mvp)


def test_pbcoreAssetType_type(validator, mvp):
    """Test pbcoreAssetType."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = 'string'
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"string" is not of type "array"'
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = 3
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '3 is not of type "array"'
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = 3.14
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '3.14 is not of type "array"'
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = None
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == 'null is not of type "array"'
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = {}
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '{} is not of type "array"'


def test_pbcoreAssetType_empty(validator, mvp):
    """Test pbcoreAssetType."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = []
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreAssetType_text(validator, mvp):
    """Test pbcoreAssetType text value"""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = [{}]
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '"text" is a required property'


def test_pbcoreAssetType_attributes(validator, mvp):
    """Test pbcoreAssetType."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = [
        {
            "text": "video",
            "source": "local",
            "ref": "video-1",
            "version": "1.0",
            "annotation": "Test video",
        }
    ]
    validator(mvp)


def test_pbcoreAssetType_invalid(validator, mvp):
    """Test pbcoreAssetType."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetType'] = [
        {"text": "video", "extra_value": "not allowed"}
    ]
    with raises(ValidationError) as error:
        validator(mvp)
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )


def test_pbcoreAssetDate(validator, mvp):
    """Test pbcoreAssetDate."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetDate'] = [{"text": "0000-00-00"}]
    validator(mvp)


def test_pbcoreAssetDate_attributes(validator, mvp):
    """Test pbcoreAssetDate attributes."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetDate'] = [
        {
            "text": "0000-00-00",
            "source": "local",
            "ref": "date-1",
            "version": "1.0",
            "annotation": "Test date",
            "dateType": "date",
        }
    ]
    validator(mvp)


def test_pbcoreAssetDate_missing(validator, mvp):
    """Test missing pbcoreAssetDate."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetDate'] = []
    with raises(ValidationError) as error:
        validator(mvp)
    assert error.value.message == '[] has less than 1 item'


def test_pbcoreAssetDate_invalid(validator, mvp):
    """Test invalid pbcoreAssetDate."""
    mvp['pbcoreDescriptionDocument']['pbcoreAssetDate'] = [
        {"text": "date", "extra_value": "not allowed"}
    ]
    with raises(ValidationError) as error:
        validator(mvp)
    assert (
        error.value.message
        == "Unevaluated properties are not allowed ('extra_value' was unexpected)"
    )
