
import sys
import re
from fastapi.testclient import TestClient

sys.path.append(".")
from main import app


client = TestClient(app)


def test_response_root():
    response = client.get("/")
    assert response.status_code == 200


def test_response_len_regions():
    response = client.get("/")
    regions_len = len(response.json()["Region"].keys())
    assert regions_len == 6

def test_codification_languages():
    response = client.get("/")
    pattern = re.compile(r'\b[0-9a-f]{40}\b')
    languages = response.json()["Language SHA1"]
    results = [ ]
    for key , value in languages.items():
        match = re.match(pattern, value)
        results.append(match)
    
    validation_codification = True

    for value in results:
        if value is None:
            validation_codification = False
    assert validation_codification == True
        
