from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_validate_xml():
    # response = client.get("/validate/xml-file", headers={"X-Token": "coneofsilence"})
    response = client.post("/validate/xml-file", files={"file": open("test/pbcore_xml/15-0c4sj19p2m.xml", "rb")})

    assert response.status_code == 200
    assert response.json() == {
        "valid": True,
        "file": filename
    }


def test_validate_xml_not_xml():
    response = client.post("/validate/xml-file")
    assert response.status_code == 400
    assert response.json() == {"detail": "REPLACE WITH ERROR MESSAGE"}

