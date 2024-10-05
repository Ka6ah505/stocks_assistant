from app.repositories.bonds.bond_repository import BondRepository
from app.services.bonds.bond_service import IBondService


class BondService(IBondService):
    async def add_bond(self, data):
        cnt = await BondRepository().add_row(data)
        return cnt
