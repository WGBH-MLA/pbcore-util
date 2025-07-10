from typing import Optional

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
    pbcoreAssetType: Optional[list[PBCoreAssetType]] = Field(None, min_length=1)
    pbcoreAssetDate: Optional[list[PBCoreAssetDate]] = Field(None, min_length=1)
    pbcoreIdentifier: list[PBCoreIdentifier] = Field(..., min_length=1)
    pbcoreTitle: list[PBCoreTitle] = Field(..., min_length=1)
    pbcoreSubject: Optional[list[PBCoreSubject]] = Field(None, min_length=1)
    pbcoreDescription: list[PBCoreDescription] = Field(..., min_length=1)
    pbcoreGenre: Optional[list[PBCoreGenre]] = Field(None, min_length=1)
    pbcoreRelation: Optional[list[PBCoreRelation]] = Field(None, min_length=1)
    pbcoreCoverage: Optional[list[PBCoreCoverage]] = Field(None, min_length=1)
    pbcoreAudienceLevel: Optional[list[PBCoreAudienceLevel]] = Field(None, min_length=1)
    pbcoreAudienceRating: Optional[list[PBCoreAudienceRating]] = Field(
        None, min_length=1
    )
    pbcoreCreator: Optional[list[PBCoreCreator]] = Field(None, min_length=1)
    pbcoreContributor: Optional[list[PBCoreContributor]] = Field(None, min_length=1)
    pbcorePublisher: Optional[list[PBCorePublisher]] = Field(None, min_length=1)
    pbcoreRightsSummary: Optional[list[PBCoreRightsSummary]] = Field(None, min_length=1)
    pbcoreInstantiation: Optional[list[PBCoreInstantiation]] = Field(None, min_length=1)
    pbcoreAnnotation: Optional[list[PBCoreAnnotation]] = Field(None, min_length=1)
    pbcorePart: Optional[list['PBCorePart']] = Field(None, min_length=1)
    pbcoreExtension: Optional[list[PBCoreExtension]] = Field(None, min_length=1)


class PBCorePart(PBCoreAttributesTime, PBCoreDescriptionDocumentSubelements):
    """PBCorePart element."""

    partType: Optional[str] = None
    partTypeSource: Optional[str] = None
    partTypeRef: Optional[str] = None
    partTypeVersion: Optional[str] = None
    partTypeAnnotation: Optional[str] = None


# Rebuild the Description Document model to ensure the recursive PBCorePart is recognized

PBCoreDescriptionDocumentSubelements.model_rebuild()


class PBCoreDescriptionDocument(
    XsiSchemaLocation, PBCoreDescriptionDocumentSubelements
):
    """Model for PBCoreDescriptionDocument subelements."""


class PBCoreCollection(XsiSchemaLocation):
    """Collection of PBCoreDescriptionDocument elements."""

    collecttionTitle: Optional[str] = None
    collectionDescription: Optional[str] = None
    collectionSource: Optional[str] = None
    collectionRef: Optional[str] = None
    collectionDate: Optional[str] = None

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
    def validate_document(cls, values):
        # Ensure only one document of any type is present
        doc_count = 0
        if values.pbcoreDescriptionDocument:
            doc_count += 1
        if values.pbcoreCollection:
            doc_count += 1
        if values.pbcoreInstantiationDocument:
            doc_count += 1
        if doc_count == 0:
            raise ValueError("At least one PBCore document type must be provided.")
        if doc_count != 1:
            raise ValueError(f"THERE CAN BE ONLY ONE!!! (PBCore Document type)")
        return values

    pbcoreDescriptionDocument: Optional[PBCoreDescriptionDocument] = None
    pbcoreCollection: Optional[PBCoreCollection] = None
    pbcoreInstantiationDocument: Optional[PBCoreInstantiationDocument] = None


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
