from fastapi import HTTPException
from pydantic import HttpUrl
from urllib.parse import urlparse
import ipaddress
import socket
import httpx

CONNECT_TIMEOUT = 5.0  # seconds
READ_TIMEOUT = 10.0  # seconds
MAX_RESPONSE_BYTES = 1_000_000  # 1 MB
FOLLOW_REDIRECTS = False


def is_public_hostname(hostname: str) -> bool:
    try:
        ip = ipaddress.ip_address(socket.gethostbyname(hostname))
        return not (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
        )
    except Exception:
        return False


async def safe_http_get(url: HttpUrl) -> str:
    """
    Fetch a URL safely, protecting against SSRF and unsafe responses.
    """
    parsed = urlparse(str(url))

    if not parsed.hostname or not is_public_hostname(parsed.hostname):
        raise HTTPException(400, "URL resolves to a restricted address")

    async with httpx.AsyncClient(
        timeout=httpx.Timeout(connect=CONNECT_TIMEOUT, read=READ_TIMEOUT),
        follow_redirects=FOLLOW_REDIRECTS,
    ) as client:
        response = await client.get(str(url))
        response.raise_for_status()

    # TODO: Needs a test for content type check, e.g. mocked response.
    content_type = response.headers.get("content-type", "")
    if ("xml" or "json") not in content_type:
        raise HTTPException(400, "Expected XML response")

    # TODO: Needs a test for response size limit, e.g. mocked response.
    content = response.text
    if len(content) > MAX_RESPONSE_BYTES:
        raise HTTPException(413, "Response too large")

    return content
