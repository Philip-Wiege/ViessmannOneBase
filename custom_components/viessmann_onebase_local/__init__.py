"""
Multiline Comment
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "viessmann_onebase_local"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('viessmann_onebase_local.Hello_World', 'Test String')
    hass.states.set('viessmann_onebase_local.Vitocal_250A.FlowTemperature', '25.00')

    # Return boolean to indicate that initialization was successfully.
    return True