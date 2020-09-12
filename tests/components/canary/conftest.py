"""Define fixtures available for all tests."""
from canary.api import Api
from pytest import fixture

from tests.async_mock import MagicMock, PropertyMock, patch


@fixture
def canary(hass):
    """Mock the CanaryApi for easier testing."""
    with patch("homeassistant.components.canary.Api") as mock_canary:
        Api.login = MagicMock(return_value=True)

        instance = mock_canary.return_value = Api(
            "test-username",
            "test-password",
            1,
        )

        instance._modes_by_name = PropertyMock(return_value={})
        instance.get_entries = MagicMock(return_value=[])
        instance.get_locations = MagicMock(return_value=[])
        instance.get_location = MagicMock(return_value=None)
        instance.get_modes = MagicMock(return_value=[])
        instance.get_readings = MagicMock(return_value=[])
        instance.set_location_mode = MagicMock(return_value=None)

        yield mock_canary