from fastapi.testclient import TestClient
from pytest import fixture

from app.main import app

client = TestClient(app)


### FIXTURES ###
@fixture
def pbcore_invalid_coverage_type():
    return open(
        "tests/sample_data/pbcore_xml/100-009w0w2t.invalid_coverage_type.xml", "rb"
    )


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
def pbcore_xml_multiple_repeatable_elements():
    return open("tests/sample_data/pbcore_xml/multiple_repeatable_elements.xml", "rb")


@fixture
def pbcore_xml_subelements():
    return open("tests/sample_data/pbcore_xml/subelements.xml", "rb")


@fixture
def pbcore_xml_subelements_with_attrs():
    return open("tests/sample_data/pbcore_xml/subelements_with_attrs.xml", "rb")


@fixture
def pbcore_xml_multiple_repeatable_elements_with_attrs():
    return open(
        "tests/sample_data/pbcore_xml/multiple_repeatable_elements_with_attrs.xml", "rb"
    )

@fixture
def pbcore_xml_with_special_characters():
    return open(
        "tests/sample_data/pbcore_xml/special_characters.xml", "rb"
    )


### TESTS ###


def test_validate_xml(valid_xml):
    response = client.post("/validate/xml-file", files={"file": valid_xml})
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["valid"]
    assert "100-009w0w2t.xml" in response_json["file"]


def test_validate_xml_invalid(pbcore_invalid_coverage_type):
    response = client.post(
        "/validate/xml-file", files={"file": pbcore_invalid_coverage_type}
    )
    assert response.status_code == 422
    response_json = response.json()
    # Assert the detail contains a general error message
    assert "PBCore XML Validation Error" in response_json["detail"]
    # Assert the erroring element is mentioned in the error message
    assert "coverageType" in response_json["detail"]


def test_validate_xml_not_xml(file_not_xml):
    response = client.post("/validate/xml-file", files={"file": file_not_xml})
    response_json = response.json()
    assert response.status_code == 422
    assert "XML Parsing Error" in response_json["detail"]


def test_convert_xml_to_json_single_repeatable_elements(
    pbcore_xml_single_repeatable_elements,
):
    response = client.post(
        "/convert/xml-to-json-file",
        files={"file": pbcore_xml_single_repeatable_elements},
    )
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
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][0][
                "creatorRole"
            ]
        )
        == 1
    )
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreContributor"]) == 1
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][0][
                "contributorRole"
            ]
        )
        == 1
    )
    assert len(response_json["pbcoreDescriptionDocument"]["pbcorePublisher"]) == 1
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][0][
                "publisherRole"
            ]
        )
        == 1
    )
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAnnotation"]) == 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreExtension"]) == 1


def test_convert_xml_to_json_multiple_repeatable_elements(
    pbcore_xml_multiple_repeatable_elements,
):
    response = client.post(
        "/convert/xml-to-json-file",
        files={"file": pbcore_xml_multiple_repeatable_elements},
    )
    assert response.status_code == 200
    response_json = response.json()

    # Now assert that all of the repeatable elements are present in the JSON and have length 1
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAssetType"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAssetDate"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreIdentifier"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreTitle"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreSubject"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreDescription"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreGenre"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreRelation"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAudienceLevel"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAudienceRating"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCreator"]) == 2
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][0][
                "creatorRole"
            ]
        )
        == 2
    )
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreContributor"]) == 2
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][0][
                "contributorRole"
            ]
        )
        == 2
    )
    assert len(response_json["pbcoreDescriptionDocument"]["pbcorePublisher"]) == 2
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][0][
                "publisherRole"
            ]
        )
        == 2
    )
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreAnnotation"]) == 2
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreExtension"]) == 2
    # Instantiations and their repeatable subelements
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"]) == 2
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
                "instantiationEssenceTrack"
            ]
        )
        == 2
    )
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
                "instantiationEssenceTrack"
            ]
        )
        == 2
    )


def test_convert_xml_to_json_multiple_repeatable_elements_with_attrs(
    pbcore_xml_multiple_repeatable_elements_with_attrs,
):
    response = client.post(
        "/convert/xml-to-json-file",
        files={"file": pbcore_xml_multiple_repeatable_elements_with_attrs},
    )
    assert response.status_code == 200
    response_json = response.json()

    # Expect 2 instantiations
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"]) == 2
    # 1st instantiation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationIdentifier"
        ][0]["text"]
        == "alpha"
    )
    # 1st instantiation; expect 2 Essence tracks
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
                "instantiationEssenceTrack"
            ]
        )
        == 2
    )
    # 1st instantiation; 1st Essence track
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][0]["essenceTrackType"]["text"]
        == "bravo"
    )
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
                "instantiationEssenceTrack"
            ][0]["essenceTrackAnnotation"]
        )
        == 2
    )
    # 1st instantiation; 1st Essence track; 1st essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][0]["annotationType"]
        == "charlie"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][0]["text"]
        == "delta"
    )
    # 1st instantiation; 1st Essence track; 2nd essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][1]["text"]
        == "foxtrot"
    )
    # 1st instantiation; 2nd Essence track
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][1]["essenceTrackType"]["text"]
        == "golf"
    )
    # 1st instantiation; 2nd Essence track; 1st essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][0]["annotationType"]
        == "hotel"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][0]["text"]
        == "india"
    )
    # 1st instantiation; 2nd Essence track; 2nd essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][1]["annotationType"]
        == "juliet"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][0][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][1]["text"]
        == "kilo"
    )
    # 2nd instantiation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationIdentifier"
        ][0]["text"]
        == "lima"
    )
    # 2nd instantiation; expect 2 Essence tracks
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
                "instantiationEssenceTrack"
            ]
        )
        == 2
    )
    # 2nd instantiation; 1st Essence track
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][0]["essenceTrackType"]["text"]
        == "mike"
    )
    assert (
        len(
            response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
                "instantiationEssenceTrack"
            ][0]["essenceTrackAnnotation"]
        )
        == 2
    )
    # 2nd instantiation; 1st Essence track; 1st essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][0]["annotationType"]
        == "november"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][0]["text"]
        == "oscar"
    )
    # 2nd instantiation; 1st Essence track; 2nd essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][1]["annotationType"]
        == "papa"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][0]["essenceTrackAnnotation"][1]["text"]
        == "quebec"
    )
    # 2nd instantiation; 2nd Essence track
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][1]["essenceTrackType"]["text"]
        == "romeo"
    )
    # 2nd instantiation; 2nd Essence track; 1st essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][0]["annotationType"]
        == "sierra"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][0]["text"]
        == "tango"
    )
    # 2nd instantiation; 2nd Essence track; 2nd essence track annotation
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][1]["annotationType"]
        == "uniform"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"][1][
            "instantiationEssenceTrack"
        ][1]["essenceTrackAnnotation"][1]["text"]
        == "victor"
    )


def test_convert_xml_to_json_subelements(pbcore_xml_subelements):
    response = client.post(
        "/convert/xml-to-json-file", files={"file": pbcore_xml_subelements}
    )
    assert response.status_code == 200
    response_json = response.json()

    # Assert propery grouping of mulitple pbcoreCoverage elements.
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"]) == 2
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][0]["coverage"][
            "text"
        ]
        == "Test Location"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][0]["coverageType"][
            "text"
        ]
        == "Spatial"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][1]["coverage"][
            "text"
        ]
        == "Test Time"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][1]["coverageType"][
            "text"
        ]
        == "Temporal"
    )

    # Assert propery grouping of mulitple pbcoreContributor elements.
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreContributor"]) == 2
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][0][
            "contributor"
        ]["text"]
        == "Test Contributor 1"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][0][
            "contributorRole"
        ][0]["text"]
        == "Test Contributor Role 1"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][1][
            "contributor"
        ]["text"]
        == "Test Contributor 2"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreContributor"][1][
            "contributorRole"
        ][0]["text"]
        == "Test Contributor Role 2"
    )

    # Assert propery grouping of mulitple pbcoreCreator elements.
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCreator"]) == 2
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][0]["creator"][
            "text"
        ]
        == "Test Creator 1"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][0]["creatorRole"][
            0
        ]["text"]
        == "Test Creator Role 1"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][1]["creator"][
            "text"
        ]
        == "Test Creator 2"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCreator"][1]["creatorRole"][
            0
        ]["text"]
        == "Test Creator Role 2"
    )

    # Assert propery grouping of mulitple pbcorePublisher elements.
    assert len(response_json["pbcoreDescriptionDocument"]["pbcorePublisher"]) == 2
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][0]["publisher"][
            "text"
        ]
        == "Test Publisher 1"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][0][
            "publisherRole"
        ][0]["text"]
        == "Test Publisher Role 1"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][1]["publisher"][
            "text"
        ]
        == "Test Publisher 2"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcorePublisher"][1][
            "publisherRole"
        ][0]["text"]
        == "Test Publisher Role 2"
    )


def test_convert_xml_to_json_subelements_with_attrs(pbcore_xml_subelements_with_attrs):
    response = client.post(
        "/convert/xml-to-json-file", files={"file": pbcore_xml_subelements_with_attrs}
    )
    assert response.status_code == 200
    response_json = response.json()

    # Assert propery grouping of mulitple pbcoreCoverage elements.
    assert len(response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"]) == 2
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][0]["coverage"][
            "text"
        ]
        == "Test Location"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][0]["coverage"][
            "startTime"
        ]
        == "test-coverage-start-time"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][0]["coverage"][
            "endTime"
        ]
        == "test-coverage-end-time"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][0]["coverageType"][
            "text"
        ]
        == "Spatial"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][1]["coverage"][
            "text"
        ]
        == "Test Time"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][1]["coverageType"][
            "text"
        ]
        == "Temporal"
    )
    assert (
        response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"][1]["coverageType"][
            "annotation"
        ]
        == "test coverage type annotation"
    )


def test_convert_xml_to_json_no_text_with_subelements(pbcore_xml_subelements):
    response = client.post(
        "/convert/xml-to-json-file",
        files={"file": pbcore_xml_subelements},
    )
    assert response.status_code == 200
    response_json = response.json()

    assert "text" not in response_json["pbcoreDescriptionDocument"]

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreRelation"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreCoverage"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreCreator"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreContributor"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcorePublisher"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreRightsSummary"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreRightsSummary"]:
        assert "text" not in element

    for element in response_json["pbcoreDescriptionDocument"]["pbcoreInstantiation"]:
        assert "text" not in element
        for instantiation in response_json["pbcoreDescriptionDocument"][
            "pbcoreInstantiation"
        ]:
            for element in instantiation["instantiationEssenceTrack"]:
                assert "text" not in element
            for element in instantiation["instantiationRights"]:
                assert "text" not in element
            for element in instantiation["instantiationRelation"]:
                assert "text" not in element


def test_convert_xml_to_json_handles_special_characters(pbcore_xml_with_special_characters):
    response = client.post(
        "/convert/xml-to-json-file",
        files={"file": pbcore_xml_with_special_characters},
    )
    assert response.status_code == 200
    response_json = response.json()

    assert response_json["pbcoreDescriptionDocument"]["pbcoreTitle"][0]['text'] == "\"quoted string\""
    assert response_json["pbcoreDescriptionDocument"]["pbcoreTitle"][1]['text'] == "\"improperly quoted string"
    assert response_json["pbcoreDescriptionDocument"]["pbcoreTitle"][2]['text'] == "\\\"previously escaped quoted string\\\""
    assert response_json["pbcoreDescriptionDocument"]["pbcoreTitle"][3]['text'] == "single \\ backslash"
    assert response_json["pbcoreDescriptionDocument"]["pbcoreTitle"][4]['text'] == "double \\\\ backslash"
    # The test below is an actual example of bad data that made it's way into
    # our production PBCore. While not ideal, we still need to make sure that
    # values like this do not result in invalid JSON when converted.
    assert response_json["pbcoreDescriptionDocument"]["pbcoreTitle"][5]['text'] == "[\"[\\\"480\\\"]\"] x [\"[\\\"360\\\"]\"]"
    



