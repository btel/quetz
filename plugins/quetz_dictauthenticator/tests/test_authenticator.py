import pytest


@pytest.mark.parametrize(
    "config_extra", ['[dictauthenticator]\nusers=["user:password"]']
)
def test_authenticator(client):
    response = client.get("/auth/dict/login")
    assert "password" in response.text
    assert "username" in response.text
