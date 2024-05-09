"""Test of surface brightness service."""

import pytest

from skybrightnessmodel.services.sbservice import SkyBrightnessService


@pytest.mark.asyncio
async def test_sbservice() -> None:
    """Test service."""
    sbservice = SkyBrightnessService()
    mag = await sbservice.get_one_skybrightness(63000.2, 240.0, -60.0, "g")
    assert 25 > mag > 20
