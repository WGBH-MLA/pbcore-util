from random import randint

default_attrs = {
    "source": "test-source",
    "ref": "https://example.org#test-ref-uri",
    "version": "1.0",
    "annotation": "Test Annotation",
}


def defaults_and_overrides(func):
    """Decorator to apply defaults and overrides to test data methods."""

    def wrapper(**overrides):
        attrs = default_attrs.copy()
        attrs.update(func())
        attrs.update(overrides)
        return attrs

    return wrapper


def test_aapb_id() -> str:
    return f"cpb-aacip-{randint(10, 999)}-{randint(10000000, 99999999)}"


def xsiSchemaLocation() -> str:
    return "http://www.pbcore.org/xsd/pbcore-2.0.xsd"


@defaults_and_overrides
def pbcoreAssetType() -> dict:
    return {
        "text": "Video",
    }


@defaults_and_overrides
def pbcoreDescriptionDocument() -> dict:
    return {
        "xsi:schemaLocation": xsiSchemaLocation(),
        "pbcoreIdentifier": [pbcoreIdentifier()],
        "pbcoreTitle": [pbcoreTitle()],
        "pbcoreDescription": [pbcoreDescription()],
        "pbcoreAssetDate": [pbcoreAssetDate()],
        "pbcoreAssetType": [pbcoreAssetType()],
    }


@defaults_and_overrides
def pbcoreTitle() -> dict:
    return {
        "text": "Test PBCore Title",
        "titleType": "test-title-type",
        "titleTypeSource": "test-title-type-source",
        "titleTypeRef": "https://example.org#test-title-type-source",
        "titleTypeVersion": "v1.0",
        "titleTypeAnnotation": "Test title type annotation",
    }


@defaults_and_overrides
def pbcoreDescription() -> dict:
    return {
        "text": "This is a test PBCore description.",
        "descriptionType": "test-description-type",
        "descriptionTypeSource": "test-description-type-source",
        "descriptionTypeRef": "https://example.org#test-description-type-source",
        "descriptionTypeVersion": "v1.0",
        "descriptionTypeAnnotation": "Test description type annotation",
    }


@defaults_and_overrides
def pbcoreAssetDate() -> dict:
    return {
        "text": "2024-01-01",
        "dateType": "creation",
    }


@defaults_and_overrides
def pbcoreSubject() -> dict:
    return {
        "text": "Test Subject",
    }


@defaults_and_overrides
def pbcoreIdentifier() -> dict:
    return {"text": test_aapb_id()}


@defaults_and_overrides
def pbcoreInstantiationDocument() -> dict:
    return {"xsi_schemalocation": xsiSchemaLocation()}


@defaults_and_overrides
def pbcoreInstantiation() -> dict:
    return {
        "instantiationIdentifier": [instantiationIdentifier()],
        "instantiationLocation": instantiationLocation(),
    }


@defaults_and_overrides
def instantiationIdentifier() -> dict:
    return {
        "text": test_aapb_id(),
    }


@defaults_and_overrides
def instantiationDate() -> dict:
    return {
        "text": "2024-01-01",
    }


@defaults_and_overrides
def instantiationDimensions() -> dict:
    return {
        "text": "1920x1080",
    }


@defaults_and_overrides
def instantiationPhysical() -> dict:
    return {"text": "test instantiation physical"}


@defaults_and_overrides
def instantiationDigital() -> dict:
    return {"text": "Test Instantiation Digital"}


@defaults_and_overrides
def instantiationStandard() -> dict:
    return {"text": "Test Instantiation Standard"}


@defaults_and_overrides
def instantiationLocation() -> dict:
    return {"text": "Test Instantiation Location"}


@defaults_and_overrides
def instantiationMediaType() -> dict:
    return {"text": "Test Instantiation MediaType"}


@defaults_and_overrides
def instantiationGenerations() -> dict:
    return {"text": "Test Instantiation Generations"}


@defaults_and_overrides
def instantiationFileSize() -> dict:
    return {"text": "Test Instantiation File Size"}


@defaults_and_overrides
def instantiationTimeStart() -> dict:
    return {"text": "Test Instantiation Time Start"}


@defaults_and_overrides
def instantiationDuration() -> dict:
    return {"text": "Test Instantiation Duration"}


@defaults_and_overrides
def instantiationDataRate() -> dict:
    return {"text": "Test Instantiation Data Rate"}


@defaults_and_overrides
def instantiationColors() -> dict:
    return {"text": "Test Instantiation Colors"}


@defaults_and_overrides
def instantiationTracks() -> dict:
    return {"text": "Test Instantiation Tracks"}


@defaults_and_overrides
def instantiationChannelConfiguration() -> dict:
    return {"text": "Test Instantiation Channel Configuration"}


@defaults_and_overrides
def instantiationLanguage() -> dict:
    return {"text": "Test Instantiation Language"}


@defaults_and_overrides
def instantiationAlternativeModes() -> dict:
    return {"text": "Test Instantiation Alternative Modes"}


@defaults_and_overrides
def instantiationEssenceTrack() -> dict:
    return {"text": "Test Instantiation Essence Track"}


@defaults_and_overrides
def instantiationRelation() -> dict:
    return {
        "instantiationRelationIdentifier": instantiationRelationIdentifier(),
        "instantiationRelationType": instantiationRelationType(),
    }


@defaults_and_overrides
def instantiationRelationIdentifier() -> dict:
    return {
        "text": test_aapb_id(),
    }


@defaults_and_overrides
def instantiationRelationType() -> dict:
    return {"text": "Test Instantiation Relation Type"}


@defaults_and_overrides
def instantiationRights() -> dict:
    return {"text": "Test Instantiation Rights"}


@defaults_and_overrides
def instantiationAnnotation() -> dict:
    return {"text": "Test Instantiation Annotation"}


@defaults_and_overrides
def pbcoreCollection() -> dict:
    return {
        "xsi:schemaLocation": xsiSchemaLocation(),
        "collectionTitle": "Test Collection Title",
        "collectionDescription": "Test Collection Description",
        "collectionSource": "Test Collection Source",
        "collectionRef": "https://example.com/test-collection-ref",
        "collectionDate": "2025-12-18",
        "pbcoreDescriptionDocument": [pbcoreDescriptionDocument()],
    }


@defaults_and_overrides
def pbcoreAnnotation() -> dict:
    return {
        "text": "Test PBCore annotation",
    }


@defaults_and_overrides
def pbcoreGenre() -> dict:
    return {
        "text": "Test Genre",
    }


@defaults_and_overrides
def essenceTrackType():
    return {
        "text": "Test track type",
    }


@defaults_and_overrides
def essenceTrackIdentifier():
    return {
        "text": test_aapb_id(),
    }


@defaults_and_overrides
def essenceTrackStandard():
    return {
        "text": "Test track standard",
    }


@defaults_and_overrides
def essenceTrackEncoding():
    return {"text": "Test track encoding"}


@defaults_and_overrides
def essenceTrackDataRate():
    return {
        "text": "5000 kbps",
    }


@defaults_and_overrides
def essenceTrackFrameRate():
    return {"text": "1920x1080"}


@defaults_and_overrides
def essenceTrackPlaybackSpeed():
    return {
        "text": "1x",
    }


@defaults_and_overrides
def essenceTrackSamplingRate():
    return {
        "text": "48000 Hz",
    }


@defaults_and_overrides
def essenceTrackBitDepth():
    return {
        "text": "24-bit",
    }


@defaults_and_overrides
def essenceTrackFrameSize():
    return {
        "text": "1920x1080",
    }


@defaults_and_overrides
def essenceTrackAspectRatio():
    return {
        "text": "16:9",
    }


@defaults_and_overrides
def essenceTrackTimeStart():
    return {
        "text": "00:00:00",
    }


@defaults_and_overrides
def essenceTrackDuration():
    return {
        "text": "00:05:00",
    }


@defaults_and_overrides
def essenceTrackLanguage():
    return {
        "text": "en",
    }


@defaults_and_overrides
def essenceTrackAnnotation():
    return {
        "text": "Test Essence Track Annotation",
    }


@defaults_and_overrides
def essenceTrackExtension():
    return {
        "text": "Test Essence Track Extension",
    }


@defaults_and_overrides
def pbcoreRelationIdentifier() -> dict:
    return {
        "text": test_aapb_id(),
    }


@defaults_and_overrides
def pbcoreRelationType() -> dict:
    return {
        "text": "Test PBCore Relation Type",
    }


@defaults_and_overrides
def coverage() -> dict:
    return {
        "text": "Spatial",
    }


@defaults_and_overrides
def pbcoreAudienceLevel() -> dict:
    return {
        "text": "General Audience",
    }


@defaults_and_overrides
def pbcoreAudienceRating() -> dict:
    return {
        "text": "PG-13",
    }


@defaults_and_overrides
def creatorRole() -> dict:
    return {
        "text": "Director",
    }


@defaults_and_overrides
def creator() -> dict:
    return {
        "text": "Test Creator",
    }


@defaults_and_overrides
def coverageType() -> dict:
    return {
        "text": "Spatial",
    }


@defaults_and_overrides
def contributor() -> dict:
    return {
        "text": "Test Contributor",
    }


@defaults_and_overrides
def contributorRole() -> dict:
    return {
        "text": "Test Contributor Role",
    }


@defaults_and_overrides
def publisher() -> dict:
    return {
        "text": "Test Publisher}",
    }


@defaults_and_overrides
def publisherRole() -> dict:
    return {
        "text": "Test Publisher Role",
    }


@defaults_and_overrides
def rightsSummary() -> dict:
    return {
        "text": "Test Rights Summray",
    }


@defaults_and_overrides
def rightsLink() -> dict:
    return {
        "text": "Test Rights Link",
    }


@defaults_and_overrides
def rightsEmbedded() -> dict:
    return {
        "text": "Test Rights Embedded",
    }


@defaults_and_overrides
def extensionElement() -> dict:
    return {
        "text": "Test Extension Element",
    }


@defaults_and_overrides
def extensionValue() -> dict:
    return {
        "text": "Test Extension Value",
    }


@defaults_and_overrides
def extensionAuthorityUsed() -> dict:
    return {
        "text": "Test Extension Authority Used",
    }


@defaults_and_overrides
def extensionWrap() -> dict:
    return {
        "extensionElement": extensionElement(),
        "extensionValue": extensionValue(),
        "extensionAuthorityUsed": extensionAuthorityUsed(),
    }


@defaults_and_overrides
def extensionEmbedded() -> dict:
    return {
        "text": "<foo>bar</foo>",
    }


@defaults_and_overrides
def pbcoreExtension() -> dict:
    return {
        "extensionWrap": [extensionWrap()],
    }
