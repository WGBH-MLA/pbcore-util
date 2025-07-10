from pydantic import Field, model_validator
from pbcore.models.base import PBCoreAttributesTime, PBCoreBaseModel, PBCoreAnnotation

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
    pbcorePart: list['PBCorePart'] | None = Field(None, min_length=1)
    pbcoreExtension: list[PBCoreExtension] | None = Field(None, min_length=1)


class PBCorePart(PBCoreAttributesTime, PBCoreDescriptionDocumentSubelements):
    """PBCorePart element."""

    partType: str | None = None
    partTypeSource: str | None = None
    partTypeRef: str | None = None
    partTypeVersion: str | None = None
    partTypeAnnotation: str | None = None


# Rebuild the Description Document model to ensure the recursive PBCorePart is recognized

PBCoreDescriptionDocumentSubelements.model_rebuild()


class PBCoreDescriptionDocument(
    XsiSchemaLocation, PBCoreDescriptionDocumentSubelements
):
    """Model for PBCoreDescriptionDocument subelements."""


class PBCoreCollection(XsiSchemaLocation):
    """Collection of PBCoreDescriptionDocument elements."""

    collectionTitle: str | None = None
    collectionDescription: str | None = None
    collectionSource: str | None = None
    collectionRef: str | None = None
    collectionDate: str | None = None

    pbcoreDescriptionDocument: list[PBCoreDescriptionDocument] = Field(
        ..., min_length=1
    )


class PBCoreInstantiationDocument(
    PBCoreAttributesTime, PBCoreDescriptionDocumentSubelements
):
    """Model for PBCoreInstantiationDocument elements."""


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
