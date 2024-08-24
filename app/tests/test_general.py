import pytest
from httpx import AsyncClient
from typing import AsyncGenerator
from main import app

# client = AsyncClient(app)
url = 'http://fastapi.localhost'


@pytest.fixture(scope='function')
async def test_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url=url) as client:
        yield client


@pytest.mark.asyncio
async def test_read_main(test_client):
    async for client in test_client:
        response = await client.get('/')
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {"message": "All right!"}
