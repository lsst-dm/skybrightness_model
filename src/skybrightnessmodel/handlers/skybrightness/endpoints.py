"""Operations for the skybrightness router."""

from typing import Annotated

from fastapi import APIRouter, Path

from skybrightnessmodel.domain.models import Band
from skybrightnessmodel.services.sbservice import SkyBrightnessService

skybrightness_router = APIRouter(tags=["skybrightness"])

type FilterNamePathParam = Annotated[
    Band,
    Path(
        ...,
        title="The filter name.",
        examples=["u", "g", "r", "i", "z", "y"],
    ),
]


@skybrightness_router.get(
    "/one/{band}",
    summary="Get the sky brightness.",
    response_model=float,
)
async def get_one_sky_brightness(
    band: FilterNamePathParam,
    mjd: float,
    ra: float,
    decl: float,
) -> float:
    skybrightness_service = SkyBrightnessService()
    return await skybrightness_service.get_one_skybrightness(
        mjd, ra, decl, band
    )
