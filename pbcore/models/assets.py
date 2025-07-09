from typing import List, Optional

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
    coverageType: Optional[CoverageType] = Field(None, min_length=1)


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
    creatorRole: Optional[List[CreatorRole]] = Field(None, min_length=1)


class Contributor(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Contributor element."""


class ContributorRole(PBCoreElement):
    """ContributorRole element."""

    portrayal: Optional[str] = None


class PBCoreContributor(PBCoreBaseModel):
    """PBCoreContributor element."""

    contributor: Contributor
    contributorRole: Optional[List[ContributorRole]] = Field(None, min_length=1)


class Publisher(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Publisher element."""


class PublisherRole(PBCoreElement):
    """PublisherRole element."""


class PBCorePublisher(PBCoreBaseModel):
    """PBCorePublisher element."""

    publisher: Publisher
    publisherRole: Optional[List[PublisherRole]] = Field(None, min_length=1)


class PBCorePart(PBCoreBaseModel):
    """PBCorePart element.

    TODO: Fixme
    """

    pass


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
    "PBCorePart",
]
