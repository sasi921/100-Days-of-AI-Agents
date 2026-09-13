from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

USER_AGENT = "100-Days-of-AI-Agents/Day-003 (+https://github.com/sasi921/100-Days-of-AI-Agents)"
MAX_DOWNLOAD_BYTES = 2_000_000


@dataclass(frozen=True)
class WebPage:
    url: str
    title: str
    text: str


def validate_public_url(url: str) -> str:
    parsed = urlparse(url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("URL must use http:// or https:// and include a hostname.")

    hostname = parsed.hostname.lower()
    if hostname == "localhost" or hostname.endswith(".local"):
        raise ValueError("Local/private hosts are not allowed.")

    try:
        ip = ipaddress.ip_address(hostname)
    except ValueError:
        ip = None

    if ip and (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved):
        raise ValueError("Private or local IP addresses are not allowed.")

    return parsed.geturl()


def extract_readable_text(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else "Untitled page"

    for tag in soup(["script", "style", "noscript", "svg", "nav", "footer", "header", "form"]):
        tag.decompose()

    container = soup.find("article") or soup.find("main") or soup.body or soup
    text = container.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return title, text.strip()


def fetch_page(url: str, timeout: float = 15.0) -> WebPage:
    safe_url = validate_public_url(url)
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"}

    with requests.get(safe_url, headers=headers, timeout=timeout, stream=True, allow_redirects=True) as response:
        response.raise_for_status()
        content_type = response.headers.get("content-type", "").lower()
        if "text/html" not in content_type and "application/xhtml+xml" not in content_type:
            raise ValueError(f"Expected an HTML page, got: {content_type or 'unknown content type'}")

        chunks: list[bytes] = []
        total = 0
        for chunk in response.iter_content(chunk_size=65536):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_DOWNLOAD_BYTES:
                raise ValueError("Page is too large for this beginner agent (2 MB limit).")
            chunks.append(chunk)

        html = b"".join(chunks).decode(response.encoding or "utf-8", errors="replace")

    title, text = extract_readable_text(html)
    if len(text) < 80:
        raise ValueError("The page did not contain enough readable text to research.")

    return WebPage(url=response.url, title=title, text=text)
