from fastapi import APIRouter

from app.db import schemas
from app.services.bonds.bond_service_impl import BondService

router = APIRouter(
    tags=["bonds"],
)


@router.post('/bonds')
async def add(detaile: schemas.Bond):
    bond = detaile.model_dump()
    count_new_rows = await BondService().add_bond(bond)
    return count_new_rows
