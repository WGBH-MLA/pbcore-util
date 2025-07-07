from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class PBCoreBaseModel(BaseModel):
    """Base class for all PBCore elements."""

    pass


class PBCoreTextElement(PBCoreBaseModel):
    """Base class for a required text elements in PBCore."""

    text: str


class PBCoreBaseAttributes(PBCoreBaseModel):
    """Base class for attributes in PBCore."""

    source: Optional[str] = None
    ref: Optional[str] = None
    version: Optional[str] = None
    annotation: Optional[str] = None


class PBCoreElement(PBCoreTextElement, PBCoreBaseAttributes):
    """Base class for PBCore elements with required text and optional attributes."""


class PBCoreIdentifier(PBCoreElement):
    """PBCore identifier element."""

    source: str = Field(..., description="Source of the identifier (required)")


class PBCoreDescription(PBCoreElement):
    text: str


class CreatorRole(PBCoreElement):
    pass


class Creator(PBCoreElement):
    pass


class PBCoreCreator(RootModel, PBCoreBaseModel):
    root: List[Creator | CreatorRole] = Field(..., min_items=1)


class InstantiationIdentifier(BaseModel):
    source: str
    text: str


class InstantiationPhysical(BaseModel):
    text: str


class InstantiationLocation(BaseModel):
    text: str


class InstantiationMediaType(BaseModel):
    text: str


class InstantiationGeneration(BaseModel):
    text: str


class InstantiationDuration(BaseModel):
    text: str


class InstantiationTracks(BaseModel):
    text: str


class InstantiationChannelConfiguration(BaseModel):
    text: str


class InstantiationAlternativeModes(BaseModel):
    text: str


class EssenceTrackType(BaseModel):
    text: str


class EssenceTrackAspectRatio(BaseModel):
    text: str


class InstantiationEssenceTrack(BaseModel):
    essenceTrackType: EssenceTrackType
    essenceTrackAspectRatio: Optional[EssenceTrackAspectRatio] = None


class InstantiationAnnotation(BaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreInstantiation(BaseModel):
    instantiationIdentifier: List[InstantiationIdentifier]
    instantiationPhysical: Optional[InstantiationPhysical] = None
    instantiationLocation: InstantiationLocation
    instantiationMediaType: Optional[InstantiationMediaType] = None
    instantiationGenerations: Optional[List[InstantiationGeneration]] = None
    instantiationDuration: Optional[InstantiationDuration] = None
    instantiationTracks: Optional[InstantiationTracks] = None
    instantiationChannelConfiguration: Optional[InstantiationChannelConfiguration] = (
        None
    )
    instantiationAlternativeModes: Optional[InstantiationAlternativeModes] = None
    instantiationEssenceTrack: Optional[List[InstantiationEssenceTrack]] = None
    instantiationAnnotation: Optional[List[InstantiationAnnotation]] = None


class PBCoreAnnotation(BaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreRelationType(BaseModel):
    source: Optional[str] = None
    text: str


class PBCoreRelationIdentifier(BaseModel):
    text: str


class PBCoreRelation(BaseModel):
    pbcoreRelationType: PBCoreRelationType
    pbcoreRelationIdentifier: PBCoreRelationIdentifier


class Coverage(BaseModel):
    text: str


class CoverageType(BaseModel):
    text: str


class PBCoreCoverage(BaseModel):
    coverage: Coverage
    coverageType: Optional[CoverageType] = None


class PBCoreAttributesTime(BaseModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timeAnnotation: Optional[str] = None


class PBCoreTitle(PBCoreElement, PBCoreAttributesTime):
    titleType: Optional[str] = None
    titleTypeSource: Optional[str] = None
    titleTypeRef: Optional[str] = None
    titleTypeVersion: Optional[str] = None
    titleTypeAnnotation: Optional[str] = None


class PBCoreSubject(PBCoreElement, PBCoreAttributesTime):
    subjectType: Optional[str] = None
    subjectTypeSource: Optional[str] = None
    subjectTypeRef: Optional[str] = None
    subjectTypeVersion: Optional[str] = None
    subjectTypeAnnotation: Optional[str] = None


class PBCoreDescriptionDocument(BaseModel):
    xsi_schemaLocation: str = Field(..., alias='xsi:schemaLocation')
    pbcoreAssetType: Optional[List[PBCoreElement]] = None
    pbcoreAssetDate: Optional[List[PBCoreElement]] = Field(None, min_items=1)
    pbcoreIdentifier: List[PBCoreIdentifier] = Field(..., min_items=1)
    pbcoreTitle: List[PBCoreTitle] = Field(..., min_items=1)
    pbcoreSubject: Optional[List[PBCoreSubject]] = None
    pbcoreDescription: List[PBCoreDescription] = Field(..., min_items=1)
    pbcoreCreator: Optional[List[PBCoreCreator]] = None
    pbcoreInstantiation: Optional[List[PBCoreInstantiation]] = None
    pbcoreAnnotation: Optional[List[PBCoreAnnotation]] = None
    pbcoreRelation: Optional[List[PBCoreRelation]] = None
    pbcoreCoverage: Optional[List[PBCoreCoverage]] = None
    pbcoreAudienceLevel: Optional[List[PBCoreElement]] = None


class PBCore(BaseModel):
    pbcoreDescriptionDocument: PBCoreDescriptionDocument
