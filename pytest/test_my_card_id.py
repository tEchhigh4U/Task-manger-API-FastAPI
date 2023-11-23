
from my_card_id import display_my_card_ID

def mock_display_my_card_ID(user_id):
    return "HK001"

def test_display_my_card_ID(monkeypatch):
    monkeypatch.setattr("my_card_id.display_my_card_ID", mock_display_my_card_ID)
    card_id = display_my_card_ID(12)
    assert card_id == "HK001"