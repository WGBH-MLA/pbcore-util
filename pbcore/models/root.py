from typing import List, Optional

from pydantic import Field
from pbcore.models.base import PBCoreBaseModel

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
    PBCoreRightsSummary,
    PBCoreAnnotation,
    PBCorePart,
    PBCoreExtension,
)
from pbcore.models.instantiations import PBCoreInstantiation


class XsiSchemaLocation(PBCoreBaseModel):
    """Custom type for xsi:schemaLocation attribute.

    TODO: Add validation for the schema location format."""

    xsi_schemaLocation: str = Field(..., alias='xsi:schemaLocation')


class PBCoreDescriptionDocument(XsiSchemaLocation):
    pbcoreAssetType: Optional[List[PBCoreAssetType]] = None
    pbcoreAssetDate: Optional[List[PBCoreAssetDate]] = Field(None, min_length=1)
    pbcoreIdentifier: List[PBCoreIdentifier] = Field(..., min_length=1)
    pbcoreTitle: List[PBCoreTitle] = Field(..., min_length=1)
    pbcoreSubject: Optional[List[PBCoreSubject]] = None
    pbcoreDescription: List[PBCoreDescription] = Field(..., min_length=1)
    pbcoreGenre: Optional[List[PBCoreGenre]] = None
    pbcoreRelation: Optional[List[PBCoreRelation]] = None
    pbcoreCoverage: Optional[List[PBCoreCoverage]] = None
    pbcoreAudienceLevel: Optional[List[PBCoreAudienceLevel]] = None
    pbcoreAudienceRating: Optional[List[PBCoreAudienceRating]] = None
    pbcoreCreator: Optional[List[PBCoreCreator]] = None
    pbcoreContributor: Optional[List[PBCoreContributor]] = None
    pbcorePublisher: Optional[List[PBCorePublisher]] = None
    pbcoreRightsSummary: Optional[List[PBCoreRightsSummary]] = None
    pbcoreInstantiation: Optional[List[PBCoreInstantiation]] = None
    pbcoreAnnotation: Optional[List[PBCoreAnnotation]] = None
    pbcorePart: Optional[List[PBCorePart]] = None
    pbcoreExtension: Optional[List[PBCoreExtension]] = None


class PBCoreCollection(XsiSchemaLocation):
    """Collection of PBCoreDescriptionDocument elements."""

    collecttionTitle: Optional[str] = None
    collectionDescription: Optional[str] = None
    collectionSource: Optional[str] = None
    collectionRef: Optional[str] = None
    collectionDate: Optional[str] = None

    pbcoreDescriptionDocument: List[PBCoreDescriptionDocument] = Field(
        ..., min_length=1
    )


class PBCore(PBCoreBaseModel):
    """Root model for PBCore documents."""

    pbcoreDescriptionDocument: PBCoreDescriptionDocument
