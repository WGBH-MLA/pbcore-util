from pydantic import Field
from pbcore.models.base import (
    PBCoreElement,
    PBCoreAttributesDateType,
    PBCoreAttributesTime,
    PBCoreAttributesAffiliation,
    PBCoreBaseModel,
)

# PBCore Assets


class PBCoreAssetType(PBCoreElement):
    """PBCoreAssetType element."""


class PBCoreAssetDate(PBCoreElement, PBCoreAttributesDateType):
    """PBCoreAssetDate element."""


class PBCoreIdentifier(PBCoreElement):
    """PBCoreIdentifier element."""

    source: str = Field(..., description="Source of the identifier (required)")


class PBCoreTitle(PBCoreElement, PBCoreAttributesTime):
    titleType: str | None = None
    titleTypeSource: str | None = None
    titleTypeRef: str | None = None
    titleTypeVersion: str | None = None
    titleTypeAnnotation: str | None = None


class PBCoreSubject(PBCoreElement, PBCoreAttributesTime):
    subjectType: str | None = None
    subjectTypeSource: str | None = None
    subjectTypeRef: str | None = None
    subjectTypeVersion: str | None = None
    subjectTypeAnnotation: str | None = None


class PBCoreDescription(PBCoreElement, PBCoreAttributesTime):
    descriptionType: str | None = None
    descriptionTypeSource: str | None = None
    descriptionTypeRef: str | None = None
    descriptionTypeVersion: str | None = None
    descriptionTypeAnnotation: str | None = None

    segmentType: str | None = None
    segmentTypeSource: str | None = None
    segmentTypeRef: str | None = None
    segmentTypeVersion: str | None = None
    segmentTypeAnnotation: str | None = None


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
    coverageType: CoverageType | None = None


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
    creatorRole: list[CreatorRole] | None = Field(None, min_length=1)


class Contributor(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Contributor element."""


class ContributorRole(PBCoreElement):
    """ContributorRole element."""

    portrayal: str | None = None


class PBCoreContributor(PBCoreBaseModel):
    """PBCoreContributor element."""

    contributor: Contributor
    contributorRole: list[ContributorRole] | None = Field(None, min_length=1)


class Publisher(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Publisher element."""


class PublisherRole(PBCoreElement):
    """PublisherRole element."""


class PBCorePublisher(PBCoreBaseModel):
    """PBCorePublisher element."""

    publisher: Publisher
    publisherRole: list[PublisherRole] | None = Field(None, min_length=1)


__all__ = [
    "PBCoreAssetType",
    "PBCoreAssetDate",
    "PBCoreIdentifier",
    "PBCoreTitle",
    "PBCoreSubject",
    "PBCoreDescription",
    "PBCoreGenre",
    "PBCoreRelation",
    "PBCoreCoverage",
    "PBCoreAudienceLevel",
    "PBCoreAudienceRating",
    "PBCoreCreator",
    "PBCoreContributor",
    "PBCorePublisher",
]
