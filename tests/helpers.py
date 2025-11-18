from pydantic import ValidationError
from typing import Any
from pbcore.models import PBCoreElement


# Assertion helper for validation errors
def assert_validation_error(
    error: ValidationError, *, expected_errors: list[dict[str, Any]]
) -> None:
    """Assert that the validation errors match the expected errors."""
    actual_errors = error.errors()

    assert len(actual_errors) == len(expected_errors), (
        f"Expected {len(expected_errors)} errors, got {len(actual_errors)};\nActual Errors: {actual_errors}"
    )
    for i, expected_error in enumerate(expected_errors):
        assert expected_error, f"Expected error at index {i} is empty"
        for err_key, err_val in expected_error.items():
            # Assert that expected error and actual error have the same keys
            assert err_key in actual_errors[i], (
                f"Expected key '{err_key}' not found in actual error {actual_errors[i]}"
            )

            if err_key == "ctx":
                assert "isinstance(err_val, dict)", (
                    f"Expected 'ctx' value to be a dict, got {type(err_val).__name__}"
                )
                # Ensure 'ctx' dict in expected error and actual error have the same values
                for ctx_key, ctx_val in err_val.items():
                    assert ctx_key in actual_errors[i]["ctx"], (
                        f"Expected ctx key '{ctx_key}' not found in actual error ctx {actual_errors[i]['ctx']}"
                    )
                    assert actual_errors[i]["ctx"][ctx_key] == ctx_val, (
                        f"Expected ctx value for key '{ctx_key}' to be '{ctx_val}', got '{actual_errors[i][err_key][ctx_key]}'"
                    )
            else:
                # Ensure expected error values match actual error values
                assert actual_errors[i][err_key] == err_val, (
                    f"Expected error value for key '{err_key}' to be '{err_val}', got '{actual_errors[i][err_key]}'"
                )


# Parameterized test data for testing list fields that are optional.
def list_fields_optional():
    """Return a list of model fields that expect lists."""
    return [
        "pbcoreAssetType",
        "pbcoreAssetDate",
        "pbcoreSubject",
        "pbcoreGenre",
        "pbcoreRelation",
        "pbcoreCoverage",
        "pbcoreAudienceLevel",
        "pbcoreAudienceRating",
        "pbcoreCreator",
        "pbcoreContributor",
        "pbcorePublisher",
        "pbcoreRightsSummary",
        "pbcoreInstantiation",
        "pbcoreAnnotation",
        "pbcorePart",
        "pbcoreExtension",
    ]


# Parameterized test data for testing list fields that are optional.
def list_fields_required():
    """Return a list of model fields that expect non-empty lists."""
    return [
        "pbcoreIdentifier",
        "pbcoreTitle",
        "pbcoreDescription",
    ]


def pbcore_element_models():
    """Generate all PBCoreElement subclasses for testing."""
    return [model for model in PBCoreElement.__subclasses__()]
