from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)
    

def test_send_message():
    request_data = {
        "to": "user@example.com",
        "subject": "string",
        "message": "string"
    }
    response = client.post(
        "/send_email/",
        json=request_data,
    )
    assert response.status_code == 200
    assert response.json() == {}
