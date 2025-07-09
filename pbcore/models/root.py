from typing import List, Optional

from pydantic import Field
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
    PBCorePart,
)
from pbcore.models.rights import PBCoreRightsSummary
from pbcore.models.extension import PBCoreExtension
from pbcore.models.instantiations import PBCoreInstantiation


class XsiSchemaLocation(PBCoreBaseModel):
    """Custom type for xsi:schemaLocation attribute.

    TODO: Add validation for the schema location format."""

    xsi_schemaLocation: str = Field(..., alias='xsi:schemaLocation')


class PBCoreDescriptionDocument(XsiSchemaLocation):
    pbcoreAssetType: Optional[List[PBCoreAssetType]] = Field(None, min_length=1)
    pbcoreAssetDate: Optional[List[PBCoreAssetDate]] = Field(None, min_length=1)
    pbcoreIdentifier: List[PBCoreIdentifier] = Field(..., min_length=1)
    pbcoreTitle: List[PBCoreTitle] = Field(..., min_length=1)
    pbcoreSubject: Optional[List[PBCoreSubject]] = Field(None, min_length=1)
    pbcoreDescription: List[PBCoreDescription] = Field(..., min_length=1)
    pbcoreGenre: Optional[List[PBCoreGenre]] = Field(None, min_length=1)
    pbcoreRelation: Optional[List[PBCoreRelation]] = Field(None, min_length=1)
    pbcoreCoverage: Optional[List[PBCoreCoverage]] = Field(None, min_length=1)
    pbcoreAudienceLevel: Optional[List[PBCoreAudienceLevel]] = Field(None, min_length=1)
    pbcoreAudienceRating: Optional[List[PBCoreAudienceRating]] = Field(
        None, min_length=1
    )
    pbcoreCreator: Optional[List[PBCoreCreator]] = Field(None, min_length=1)
    pbcoreContributor: Optional[List[PBCoreContributor]] = Field(None, min_length=1)
    pbcorePublisher: Optional[List[PBCorePublisher]] = Field(None, min_length=1)
    pbcoreRightsSummary: Optional[List[PBCoreRightsSummary]] = Field(None, min_length=1)
    pbcoreInstantiation: Optional[List[PBCoreInstantiation]] = Field(None, min_length=1)
    pbcoreAnnotation: Optional[List[PBCoreAnnotation]] = Field(None, min_length=1)
    pbcorePart: Optional[List[PBCorePart]] = Field(None, min_length=1)
    pbcoreExtension: Optional[List[PBCoreExtension]] = Field(None, min_length=1)


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


class PBCoreInstantiationDocument(PBCoreAttributesTime):
    """Model for PBCoreInstantiationDocument elements.

    TODO: Add subelements
    """


class PBCore(PBCoreBaseModel):
    """Root model for PBCore documents.

    TODO: Allow pbcoreCollection and pbcoreInstantiationDocument,
    but only allow one document of any kind
    """

    pbcoreDescriptionDocument: PBCoreDescriptionDocument
    # pbcoreCollection: Optional[PBCoreCollection] = None
    # pbcoreInstantiationDocument: Optional[List[PBCoreInstantiationDocument]] = None
