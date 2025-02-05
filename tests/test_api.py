import pytest
import httpx

@pytest.fixture
async def test_client():
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        yield client

@pytest.mark.asyncio
async def test_home(test_client):
    response = await test_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Balloon de Oro API"
