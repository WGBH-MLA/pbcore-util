from fastapi.testclient import TestClient
from pytest import fixture

from app.main import app

client = TestClient(app)


### FIXTURES ###
@fixture
def pbcore_invalid_coverage_type():
    return open("tests/sample_data/pbcore_xml/100-009w0w2t.invalid_coverage_type.xml", "rb")

@fixture
def valid_xml():
    return open("tests/sample_data/pbcore_xml/100-009w0w2t.xml", "rb")

@fixture
def file_not_xml():
    return open("tests/sample_data/not_xml.txt", "rb")

@fixture
def pbcore_xml_single_repeatable_elements():
    return open("tests/sample_data/pbcore_xml/single_repeatable_elements.xml", "rb")

@fixture
def pbcore_xml_all_roles():
    return open("tests/sample_data/pbcore_xml/all_roles.xml", "rb")

### TESTS ###

def test_validate_xml(valid_xml):
    response = client.post("/validate/xml-file", files={"file": valid_xml})
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['valid'] == True
    assert "100-009w0w2t.xml" in response_json['file']


def test_validate_xml_invalid(pbcore_invalid_coverage_type):
    response = client.post("/validate/xml-file", files={"file": pbcore_invalid_coverage_type})
    assert response.status_code == 422
    response_json = response.json()
    # Assert the detail contains a general error message
    assert "PBCore XML Validation Error" in response_json['detail']
    # Assert the erroring element is mentioned in the error message
    assert "coverageType" in response_json["detail"]


def test_validate_xml_not_xml(file_not_xml):
    response = client.post("/validate/xml-file", files={"file": file_not_xml})
    response_json = response.json()
    assert response.status_code == 422
    assert "XML Parsing Error" in response_json['detail']

def test_convert_xml_to_json_single_repeatable_elements(pbcore_xml_single_repeatable_elements):
    response = client.post("/convert/xml-to-json-file", files={"file": pbcore_xml_single_repeatable_elements})
    assert response.status_code == 200
    response_json = response.json()

    # Now assert that all of the repeatable elements are present in the JSON and have length 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAssetType"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAssetDate"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreIdentifier"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreTitle"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreSubject"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreDescription"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreGenre"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreRelation"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAudienceLevel"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAudienceRating"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCreator"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][0]["creatorRole"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreContributor"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][0]["contributorRole"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcorePublisher"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][0]["publisherRole"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAnnotation"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreExtension"]) == 1

    
def test_convert_xml_to_json_grouping(pbcore_xml_all_roles):
    response = client.post("/convert/xml-to-json-file", files={"file": pbcore_xml_all_roles})
    assert response.status_code == 200
    response_json = response.json()