from pytest import fixture
from tests import pbcore_test_data as td


@fixture
def model_factory():
    """Factory fixture to create PBCore model instances with test data."""

    def _factory(model, **overrides):
        import re

        # Look for a method in the pbcore_test_data module that matches the
        # model name converted to lower camelcase, e.g. PBCoreDescriptionDocument -> pbcoreDescriptionDocument
        test_data_method_name = re.sub(
            r"([A-Z]+)", lambda m: m.group(1).lower(), model.__name__, count=1
        )

        # Get the test data method from the pbcore_test_data module.
        test_data_method = getattr(td, test_data_method_name)

        # Generate test data for the model, applying any overrides.
        model_test_data = test_data_method(**overrides)

        # Return a new instance of the model initialized with the test data.
        return model(**model_test_data)

    return _factory
