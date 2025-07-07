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


class PBCoreRepeatableElement(RootModel):
    """Base class for repeatable PBCore elements."""

    root: List[PBCoreElement] = Field(..., min_items=1)


class PBCoreIdentifier(PBCoreElement):
    """PBCore identifier element."""

    source: str = Field(..., description="Source of the identifier (required)")


class PBCoreDescriptionItem(PBCoreElement):
    text: str


class CreatorRole(PBCoreElement):
    pass


class Creator(PBCoreElement):
    pass


class PBCoreCreator(RootModel, PBCoreBaseModel):
    root: List[Creator | CreatorRole] = Field(..., min_items=1)


class InstantiationIdentifierItem(BaseModel):
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


class InstantiationEssenceTrackItem(BaseModel):
    essenceTrackType: EssenceTrackType
    essenceTrackAspectRatio: Optional[EssenceTrackAspectRatio] = None


class InstantiationAnnotationItem(BaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreInstantiationItem(BaseModel):
    instantiationIdentifier: List[InstantiationIdentifierItem]
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
    instantiationEssenceTrack: Optional[List[InstantiationEssenceTrackItem]] = None
    instantiationAnnotation: Optional[List[InstantiationAnnotationItem]] = None


class PBCoreAnnotationItem(BaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreRelationType(BaseModel):
    source: Optional[str] = None
    text: str


class PBCoreRelationIdentifier(BaseModel):
    text: str


class PBCoreRelationItem(BaseModel):
    pbcoreRelationType: PBCoreRelationType
    pbcoreRelationIdentifier: PBCoreRelationIdentifier


class Coverage(BaseModel):
    text: str


class CoverageType(BaseModel):
    text: str


class PBCoreCoverageItem(BaseModel):
    coverage: Coverage
    coverageType: Optional[CoverageType] = None


class PBCoreAttributesTime(BaseModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timeAnnotation: Optional[str] = None


class PBCoreTitleItem(PBCoreElement, PBCoreAttributesTime):
    titleType: Optional[str] = None
    titleTypeSource: Optional[str] = None
    titleTypeRef: Optional[str] = None
    titleTypeVersion: Optional[str] = None
    titleTypeAnnotation: Optional[str] = None


class PBCoreSubjectItem(PBCoreElement, PBCoreAttributesTime):
    subjectType: Optional[str] = None
    subjectTypeSource: Optional[str] = None
    subjectTypeRef: Optional[str] = None
    subjectTypeVersion: Optional[str] = None
    subjectTypeAnnotation: Optional[str] = None


class PBCoreDescriptionDocument(BaseModel):
    xsi_schemaLocation: str = Field(..., alias='xsi:schemaLocation')
    pbcoreAssetType: Optional[PBCoreRepeatableElement] = None
    pbcoreAssetDate: Optional[List[PBCoreElement]] = Field(None, min_items=1)
    pbcoreIdentifier: List[PBCoreIdentifier] = Field(..., min_items=1)
    pbcoreTitle: List[PBCoreTitleItem] = Field(..., min_items=1)
    pbcoreSubject: Optional[List[PBCoreSubjectItem]] = None
    pbcoreDescription: List[PBCoreDescriptionItem] = Field(..., min_items=1)
    pbcoreCreator: Optional[List[PBCoreCreator]] = None
    pbcoreInstantiation: Optional[List[PBCoreInstantiationItem]] = None
    pbcoreAnnotation: Optional[List[PBCoreAnnotationItem]] = None
    pbcoreRelation: Optional[List[PBCoreRelationItem]] = None
    pbcoreCoverage: Optional[List[PBCoreCoverageItem]] = None
    pbcoreAudienceLevel: Optional[PBCoreRepeatableElement] = None


class PBCore(BaseModel):
    pbcoreDescriptionDocument: PBCoreDescriptionDocument
