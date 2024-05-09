"""Test of sky brightness domain."""

from skybrightnessmodel.domain.models import SkyModel


def test_domain() -> None:
    """Test domain."""
    sky_model = SkyModel(
        init_load_length=1,
        load_length=1,
    )
    mag = sky_model.get_mag(63000.2, 240.0, -60.0, "g")
    assert 25 > mag > 20
