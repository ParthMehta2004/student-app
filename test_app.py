from app import app

def test_home():
    client = app.test_client()
    assert client.get("/").status_code == 200

def test_health():
    client = app.test_client()
    assert client.get("/health").status_code == 200

def test_add_student():
    client = app.test_client()
    r = client.post("/students", json={"name": "Parth", "course": "CSE"})
    assert r.status_code == 201