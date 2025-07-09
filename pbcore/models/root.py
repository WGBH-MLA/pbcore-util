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


class PBCoreDescriptionDocument(PBCoreBaseModel):
    xsi_schemaLocation: str = Field(..., alias='xsi:schemaLocation')
    pbcoreAssetType: Optional[List[PBCoreAssetType]] = None
    pbcoreAssetDate: Optional[List[PBCoreAssetDate]] = Field(None, min_items=1)
    pbcoreIdentifier: List[PBCoreIdentifier] = Field(..., min_items=1)
    pbcoreTitle: List[PBCoreTitle] = Field(..., min_items=1)
    pbcoreSubject: Optional[List[PBCoreSubject]] = None
    pbcoreDescription: List[PBCoreDescription] = Field(..., min_items=1)
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


class PBCore(PBCoreBaseModel):
    pbcoreDescriptionDocument: PBCoreDescriptionDocument
