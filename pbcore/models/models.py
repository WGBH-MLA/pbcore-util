from typing import List, Optional

from pydantic import BaseModel, Field, RootModel

# Base classes for PBCore elements


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


class PBCoreAttributesDateType(PBCoreBaseModel):
    dateType: Optional[str] = None


class PBCoreAttributesTime(PBCoreBaseModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timeAnnotation: Optional[str] = None


class PBCoreAttributesAffiliation(PBCoreBaseModel):
    affiliation: Optional[str] = None
    affiliationSource: Optional[str] = None
    affiliationRef: Optional[str] = None
    affiliationVersion: Optional[str] = None
    affiliationAnnotation: Optional[str] = None


class PBCoreElement(PBCoreTextElement, PBCoreBaseAttributes):
    """Base class for PBCore elements with required text and optional attributes."""


# PBCore Assets


class PBCoreAssetType(PBCoreElement):
    """PBCoreAssetType element."""


class PBCoreAssetDate(PBCoreElement, PBCoreAttributesDateType):
    """PBCoreAssetDate element."""


class PBCoreIdentifier(PBCoreElement):
    """PBCoreIdentifier element."""

    source: str = Field(..., description="Source of the identifier (required)")


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


class PBCoreDescription(PBCoreElement, PBCoreAttributesTime):
    descriptionType: Optional[str] = None
    descriptionTypeSource: Optional[str] = None
    descriptionTypeRef: Optional[str] = None
    descriptionTypeVersion: Optional[str] = None
    descriptionTypeAnnotation: Optional[str] = None

    segmentType: Optional[str] = None
    segmentTypeSource: Optional[str] = None
    segmentTypeRef: Optional[str] = None
    segmentTypeVersion: Optional[str] = None
    segmentTypeAnnotation: Optional[str] = None


class PBCoreGenre(PBCoreElement, PBCoreAttributesTime):
    """PBCore Genre element."""


class PBCoreRelationType(PBCoreElement):
    """PBCoreRelationType element."""


class PBCoreRelationIdentifier(PBCoreElement):
    """PBCoreRelationIdentifier element."""


class PBCoreRelation(PBCoreBaseModel):
    """PBCore Relation element."""

    pbcoreRelationType: PBCoreRelationType
    pbcoreRelationIdentifier: PBCoreRelationIdentifier


class Coverage(PBCoreElement, PBCoreAttributesTime):
    """Coverage element."""


class CoverageType(PBCoreElement):
    """CoverageType element."""


class PBCoreCoverage(PBCoreBaseModel):
    """PBCoreCoverage element."""

    coverage: Coverage
    coverageType: Optional[CoverageType] = None


class PBCoreAudienceLevel(PBCoreElement):
    """PBCoreAudienceLevel element."""


class PBCoreAudienceRating(PBCoreElement):
    """PBCoreAudienceRating element."""


class Creator(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Creator element."""


class CreatorRole(PBCoreElement):
    """CreatorRole element."""


class PBCoreCreator(PBCoreBaseModel):
    """PBCoreCreator element."""

    creator: Creator
    creatorRole: Optional[List[CreatorRole]] = None


class Contributor(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Contributor element."""


class ContributorRole(PBCoreElement):
    """ContributorRole element."""

    portrayal: Optional[str] = None


class PBCoreContributor(PBCoreBaseModel):
    """PBCoreContributor element."""

    contributor: Contributor
    contributorRole: Optional[List[ContributorRole]] = None


class Publisher(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Publisher element."""


class PublisherRole(PBCoreElement):
    """PublisherRole element."""


class PBCorePublisher(PBCoreBaseModel):
    """PBCorePublisher element."""

    publisher: Publisher
    publisherRole: Optional[List[PublisherRole]] = None


class RightsSummary(PBCoreElement):
    """RightsSummary element."""


class RightsLink(PBCoreElement):
    """RightsLink element."""


class RightsEmbedded(PBCoreElement):
    """RightsEmbedded element."""


class PBCoreRightsSummary(PBCoreAttributesTime):
    """PBCoreRightsSummary element.

    TODO: Validate that only one type of rightsSummary, rightsLink, or rightsEmbedded are present.
    """

    rightsSummary: Optional[List[RightsSummary]] = None
    rightsLink: Optional[List[RightsLink]] = None
    rightsEmbedded: Optional[List[RightsEmbedded]] = None


class PBCorePart(PBCoreBaseModel):
    """PBCorePart element.

    TODO: Fixme
    """

    pass


class PBCoreAnnotation(PBCoreElement):
    """PBCoreAnnotation element."""

    annotationType: Optional[str] = None


class ExtensionElement(PBCoreTextElement):
    """ExtensionElement element."""


class ExtensionValue(PBCoreTextElement):
    """ExtensionValue element."""


class ExtensionAuthorityUsed(PBCoreTextElement):
    """ExtensionAuthorityUsed element."""


class ExtensionWrap(PBCoreBaseAttributes):
    """ExtensionWrap element."""

    extensionElement: ExtensionElement
    extensionValue: ExtensionValue
    extensionAuthorityUsed: Optional[ExtensionAuthorityUsed] = None


class ExtensionEmbedded(PBCoreBaseAttributes):
    """ExtensionEmbedded element."""


class PBCoreExtension(PBCoreBaseModel):
    """PBCoreExtension element.

    TODO: Validate that extensionWrap and extensionEmbedded are not both present."""

    extensionWrap: Optional[ExtensionWrap] = None
    extensionEmbedded: Optional[ExtensionEmbedded] = None


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
