import pytest
from fastapi import HTTPException
from pydantic import HttpUrl

from security.url_fetch import safe_fetch_url


@pytest.mark.asyncio
async def test_rejects_private_ip():
    url = HttpUrl("http://127.0.0.1/secret")
    with pytest.raises(HTTPException) as exc:
        await safe_fetch_url(url)

    assert exc.value.status_code == 400


@pytest.mark.asyncio
async def test_rejects_metadata_ip():
    url = HttpUrl("http://169.254.169.254/latest/meta-data")
    with pytest.raises(HTTPException):
        await safe_fetch_url(url)
