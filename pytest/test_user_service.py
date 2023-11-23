from user_service import get_username

def mock_get_username(user_id):
    return "Test User"

def test_get_username(monkeypatch):
    # replace 'get_username' with 'mock_get_username'
    monkeypatch.setattr("user_service.get_username", mock_get_username)
    username = get_username(123)
    assert get_username() == "Test User"
