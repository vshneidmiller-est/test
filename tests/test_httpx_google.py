import httpx

def test_google_status():
    """Test that a GET request to Google returns status 200 (SSL verification disabled)."""
    response = httpx.get("https://www.google.com/", verify=False)
    assert response.status_code == 200
