from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "viessmann_onebase_local"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.states.set('viessmann_onebase_local.Hello_World', 'Test String')
    hass.states.set('viessmann_onebase_local.Vitocal_250A.FlowTemperature', '25.00')

    return True