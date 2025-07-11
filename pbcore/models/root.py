from pydantic import Field, model_validator
from pbcore.models.base import PBCoreAttributesTime, PBCoreBaseModel, PBCoreAnnotation
from typing import List
from pbcore.models.assets import (
    PBCoreAssetType,
    PBCoreAssetDate,
    PBCoreIdentifier,
    PBCoreTitle,
    PBCoreSubject,
    PBCoreDescription,
    PBCoreGenre,
    PBCoreRelation,
    PBCoreCoverage,
    PBCoreAudienceLevel,
    PBCoreAudienceRating,
    PBCoreCreator,
    PBCoreContributor,
    PBCorePublisher,
)
from pbcore.models.rights import PBCoreRightsSummary
from pbcore.models.extension import PBCoreExtension
from pbcore.models.instantiations import PBCoreInstantiation


class XsiSchemaLocation(PBCoreBaseModel):
    """Custom type for xsi:schemaLocation attribute.

    TODO: Add validation for the schema location format."""

    xsi_schemaLocation: str = Field(..., alias='xsi:schemaLocation')


class PBCoreDescriptionDocumentSubelements(PBCoreBaseModel):
    pbcoreAssetType: list[PBCoreAssetType] | None = Field(None, min_length=1)
    pbcoreAssetDate: list[PBCoreAssetDate] | None = Field(None, min_length=1)
    pbcoreIdentifier: list[PBCoreIdentifier] = Field(..., min_length=1)
    pbcoreTitle: list[PBCoreTitle] = Field(..., min_length=1)
    pbcoreSubject: list[PBCoreSubject] | None = Field(None, min_length=1)
    pbcoreDescription: list[PBCoreDescription] = Field(..., min_length=1)
    pbcoreGenre: list[PBCoreGenre] | None = Field(None, min_length=1)
    pbcoreRelation: list[PBCoreRelation] | None = Field(None, min_length=1)
    pbcoreCoverage: list[PBCoreCoverage] | None = Field(None, min_length=1)
    pbcoreAudienceLevel: list[PBCoreAudienceLevel] | None = Field(None, min_length=1)
    pbcoreAudienceRating: list[PBCoreAudienceRating] | None = Field(None, min_length=1)
    pbcoreCreator: list[PBCoreCreator] | None = Field(None, min_length=1)
    pbcoreContributor: list[PBCoreContributor] | None = Field(None, min_length=1)
    pbcorePublisher: list[PBCorePublisher] | None = Field(None, min_length=1)
    pbcoreRightsSummary: list[PBCoreRightsSummary] | None = Field(None, min_length=1)
    pbcoreInstantiation: list[PBCoreInstantiation] | None = Field(None, min_length=1)
    pbcoreAnnotation: list[PBCoreAnnotation] | None = Field(None, min_length=1)
    pbcorePart: List['PBCorePart'] | None = Field(None, min_length=1)
    pbcoreExtension: list[PBCoreExtension] | None = Field(None, min_length=1)


class PBCorePart(PBCoreAttributesTime, PBCoreDescriptionDocumentSubelements):
    """PBCorePart element.
    
    Definition: The pbcorePartType schema type uses a common structure for representing intellectual content parts or segments.
    """

    partType: str | None = Field(None, description="The type of part or segment")
    partTypeSource: str | None = Field(None, description="The source of the part type")
    partTypeRef: str | None = Field(None, description="Reference URI for the part type")
    partTypeVersion: str | None = Field(None, description="Version of the part type")
    partTypeAnnotation: str | None = Field(None, description="Annotation for the part type")


# Rebuild the Description Document model to ensure the recursive PBCorePart is recognized

PBCoreDescriptionDocumentSubelements.model_rebuild()


class PBCoreDescriptionDocument(
    XsiSchemaLocation, PBCoreDescriptionDocumentSubelements
):
    """Model for PBCoreDescriptionDocument subelements.
    
    Definition: the pbcoreDescriptionDocument element is a root XML element for the expression of an individual PBCore record.
    pbcoreDescriptionDocument can be used to express intellectual content only (e.g. a series or collection level record with 
    no associated instantiations), or intellectual content with one or more instantiations (e.g. an episode of a program with 
    copies/instantiations on videotape and digital file). This element is only applicable to XML expressions of PBCore.
    """


class PBCoreCollection(XsiSchemaLocation):
    """Collection of PBCoreDescriptionDocument elements.
    
    Definition: The pbcoreCollection element groups multiple pbcoreDescriptionDocument XML into one container element to allow for a
    serialized output. Uses might include API returns or other web service output.
    
    Best practice: This element is not intended to be equivalent to the archive/library concept of a 'collection.' Please see
    pbcoreAssetType for information on how PBCore can be used to express information about collections. The element is only applicable to XML expressions of PBCore. This
    container enables a similar function to RSS; pbcoreCollection would be similar to rss:channel and pbcoreDescription document to rss:item.
    """

    collectionTitle: str | None = Field(None, description="The collectionTitle attribute is a string that contains a title for the collection")
    collectionDescription: str | None = Field(None, description="The collectionDescription attribute is a string that contains a description of the collection")
    collectionSource: str | None = Field(None, description="The collectionSource attribute identifies the authority, standard, or particular controlled vocabulary used when populating the collection")
    collectionRef: str | None = Field(None, description="The collectionRef attribute provides a URI that relates to the collection")
    collectionDate: str | None = Field(None, description="The collectionDate attribute provides the date of the collection")

    pbcoreDescriptionDocument: list[PBCoreDescriptionDocument] = Field(
        ..., min_length=1
    )


class PBCoreInstantiationDocument(
    PBCoreAttributesTime, PBCoreDescriptionDocumentSubelements
):
    """Model for PBCoreInstantiationDocument elements.
    
    Definition: The pbcoreInstantiation element is the equivalent of the instantiation element, but used for the expression of an
    instantiation record at the root of an XML document. This is most commonly used when referenced from other schemas, or if you want to create and express a single,
    stand-alone instantiation.
    
    Best practice: This is most commonly used when Intellectual Content (in other words, descriptive metadata) is not expressed using
    PBCore, but rather another standard such as MODS or Dublin Core.
    """


class PBCore(PBCoreBaseModel):
    """Root model for PBCore documents."""

    @model_validator(mode='after')
    def validate_document(self):
        # Ensure only one document of any type is present
        doc_count = 0
        if self.pbcoreDescriptionDocument:
            doc_count += 1
        if self.pbcoreCollection:
            doc_count += 1
        if self.pbcoreInstantiationDocument:
            doc_count += 1
        if doc_count == 0:
            raise ValueError("At least one PBCore document type must be provided.")
        if doc_count != 1:
            raise ValueError(f"THERE CAN BE ONLY ONE!!! (PBCore Document type)")
        return self

    pbcoreDescriptionDocument: PBCoreDescriptionDocument | None = None
    pbcoreCollection: PBCoreCollection | None = None
    pbcoreInstantiationDocument: PBCoreInstantiationDocument | None = None


"""Minimal Viable PBCore Description Document structure."""
mvp = {
    "pbcoreDescriptionDocument": {
        "xsi:schemaLocation": "http://www.example.com/schema",
        "pbcoreIdentifier": [{"text": "123", "source": "example"}],
        "pbcoreTitle": [{"text": "Title"}],
        "pbcoreDescription": [{"text": ""}],
    },
}

__all__ = [
    "PBCore",
    "PBCoreDescriptionDocument",
    "PBCoreCollection",
    "PBCoreInstantiationDocument",
    "PBCorePart",
    "mvp",
]
