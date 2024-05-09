"""Models for sky brightness domain."""

from enum import Enum

import healpy as hp
from rubin_scheduler.skybrightness_pre import SkyModelPre

__all__ = ["Band", "SkyModel"]


class Band(str, Enum):
    """Supported filters."""

    u = "u"
    g = "g"
    r = "r"
    i = "i"
    z = "z"
    y = "y"


class SkyModel(SkyModelPre):
    """Sky brightness domain model."""

    def get_mag(self, mjd: float, ra: float, decl: float, band: Band) -> float:
        hpix = hp.ang2pix(self.nside, ra, decl, lonlat=True)
        return self.return_mags(mjd)[band][hpix].item()
