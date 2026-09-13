import pytest

from web_tool import extract_readable_text, validate_public_url


def test_extract_readable_text_removes_navigation_and_scripts():
    html = """
    <html><head><title>Agent Guide</title><script>ignore me</script></head>
    <body><nav>Menu</nav><main><h1>Agents</h1><p>AI agents can use tools to gather grounded information.</p>
    <p>Grounded systems connect model reasoning to external evidence.</p></main><footer>Footer</footer></body></html>
    """
    title, text = extract_readable_text(html)
    assert title == "Agent Guide"
    assert "AI agents" in text
    assert "ignore me" not in text
    assert "Menu" not in text


def test_validate_public_url_rejects_local_hosts():
    with pytest.raises(ValueError):
        validate_public_url("http://localhost:8000/private")
    with pytest.raises(ValueError):
        validate_public_url("http://127.0.0.1/private")


def test_validate_public_url_accepts_https():
    assert validate_public_url("https://example.com/article") == "https://example.com/article"
