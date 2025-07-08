from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class PBCoreBaseModel(BaseModel):
    """Base class for all PBCore elements."""


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


class Creator(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """PBCore creator element."""


class CreatorRole(PBCoreElement):
    """PBCore creator role element."""


class PBCoreCreator(RootModel, PBCoreBaseModel):
    root: List[Creator | CreatorRole] = Field(..., min_items=1)


class InstantiationIdentifier(PBCoreBaseModel):
    source: str
    text: str


class InstantiationPhysical(PBCoreBaseModel):
    text: str


class InstantiationLocation(PBCoreBaseModel):
    text: str


class InstantiationMediaType(PBCoreBaseModel):
    text: str


class InstantiationGeneration(PBCoreBaseModel):
    text: str


class InstantiationDuration(PBCoreBaseModel):
    text: str


class InstantiationTracks(PBCoreBaseModel):
    text: str


class InstantiationChannelConfiguration(PBCoreBaseModel):
    text: str


class InstantiationAlternativeModes(PBCoreBaseModel):
    text: str


class EssenceTrackType(PBCoreBaseModel):
    text: str


class EssenceTrackAspectRatio(PBCoreBaseModel):
    text: str


class InstantiationEssenceTrack(PBCoreBaseModel):
    essenceTrackType: EssenceTrackType
    essenceTrackAspectRatio: Optional[EssenceTrackAspectRatio] = None


class InstantiationAnnotation(PBCoreBaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreInstantiation(PBCoreBaseModel):
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


class PBCoreAnnotation(PBCoreBaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreRelationType(PBCoreBaseModel):
    source: Optional[str] = None
    text: str


class PBCoreRelationIdentifier(PBCoreBaseModel):
    text: str


class PBCoreRelation(PBCoreBaseModel):
    pbcoreRelationType: PBCoreRelationType
    pbcoreRelationIdentifier: PBCoreRelationIdentifier


class Coverage(PBCoreBaseModel):
    text: str


class CoverageType(PBCoreBaseModel):
    text: str


class PBCoreCoverage(PBCoreBaseModel):
    coverage: Coverage
    coverageType: Optional[CoverageType] = None


class PBCoreAttributesTime(PBCoreBaseModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timeAnnotation: Optional[str] = None


class PBCoreAttributesAffiliation(PBCoreBaseModel):
    affiliation: Optional[str] = None
    affiliationSource: Optional[str] = None
    affiliationRef: Optional[str] = None
    affiliationVersion: Optional[str] = None


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


class PBCoreDescriptionDocument(PBCoreBaseModel):
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


class PBCore(PBCoreBaseModel):
    pbcoreDescriptionDocument: PBCoreDescriptionDocument
