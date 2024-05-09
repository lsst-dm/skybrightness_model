"""The sky brightness service."""

from ..domain.models import Band, SkyModel

__all__ = ["SkyBrightnessService"]


class SkyBrightnessService:
    """A service for orchestrating the sky brightness domain server."""

    def __init__(self) -> None:
        self._sky_model_pre = SkyModel(
            init_load_length=1,
            load_length=1,
        )

    async def get_one_skybrightness(
        self, mjd: float, ra: float, decl: float, band: Band
    ) -> float:
        return self._sky_model_pre.get_mag(mjd, ra, decl, band)
