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
    """PBCoreAssetType element.
    
    Definition: The pbcoreAssetType element is used to identify the type of intellectual content being described.
    """


class PBCoreAssetDate(PBCoreElement, PBCoreAttributesDateType):
    """PBCoreAssetDate element.
    
    Definition: The pbcoreAssetDate element is used to represent dates associated with the intellectual content being described.
    """


class PBCoreIdentifier(PBCoreElement):
    """PBCoreIdentifier element.
    
    Definition: The pbcoreIdentifier element is used to assign an unambiguous reference to the media item being described.
    """

    source: str = Field(..., description="Source of the identifier (required)")


class PBCoreTitle(PBCoreElement, PBCoreAttributesTime):
    """PBCoreTitle element.
    
    Definition: The pbcoreTitle element is used to assign a title to the media item being described.
    """
    
    titleType: str | None = Field(None, description="The type of title")
    titleTypeSource: str | None = Field(None, description="The source of the title type")
    titleTypeRef: str | None = Field(None, description="Reference URI for the title type")
    titleTypeVersion: str | None = Field(None, description="Version of the title type")
    titleTypeAnnotation: str | None = Field(None, description="Annotation for the title type")


class PBCoreSubject(PBCoreElement, PBCoreAttributesTime):
    """PBCoreSubject element.
    
    Definition: The pbcoreSubject element is used to assign subject headings and/or keywords that describe and identify the intellectual content.
    """
    
    subjectType: str | None = Field(None, description="The type of subject")
    subjectTypeSource: str | None = Field(None, description="The source of the subject type")
    subjectTypeRef: str | None = Field(None, description="Reference URI for the subject type")
    subjectTypeVersion: str | None = Field(None, description="Version of the subject type")
    subjectTypeAnnotation: str | None = Field(None, description="Annotation for the subject type")


class PBCoreDescription(PBCoreElement, PBCoreAttributesTime):
    """PBCoreDescription element.
    
    Definition: The pbcoreDescription element is used to capture and record the who, what, when, where, why about the intellectual content.
    """
    
    descriptionType: str | None = Field(None, description="The type of description")
    descriptionTypeSource: str | None = Field(None, description="The source of the description type")
    descriptionTypeRef: str | None = Field(None, description="Reference URI for the description type")
    descriptionTypeVersion: str | None = Field(None, description="Version of the description type")
    descriptionTypeAnnotation: str | None = Field(None, description="Annotation for the description type")

    segmentType: str | None = Field(None, description="The type of segment")
    segmentTypeSource: str | None = Field(None, description="The source of the segment type")
    segmentTypeRef: str | None = Field(None, description="Reference URI for the segment type")
    segmentTypeVersion: str | None = Field(None, description="Version of the segment type")
    segmentTypeAnnotation: str | None = Field(None, description="Annotation for the segment type")


class PBCoreGenre(PBCoreElement, PBCoreAttributesTime):
    """PBCore Genre element.
    
    Definition: The pbcoreGenre element is used to describe the genre of the intellectual content being described.
    """


class PBCoreRelationType(PBCoreElement):
    """PBCoreRelationType element.
    
    Definition: The pbcoreRelationType element is used to define the relationship between the item being described and another item.
    """


class PBCoreRelationIdentifier(PBCoreElement):
    """PBCoreRelationIdentifier element.
    
    Definition: The pbcoreRelationIdentifier element is used to identify the related item.
    """


class PBCoreRelation(PBCoreBaseModel):
    """PBCore Relation element.
    
    Definition: The pbcoreRelation element is used to identify and describe relationships between the media item being described and other media items.
    """

    pbcoreRelationType: PBCoreRelationType
    pbcoreRelationIdentifier: PBCoreRelationIdentifier


class Coverage(PBCoreElement, PBCoreAttributesTime):
    """Coverage element.
    
    Definition: The coverage element describes the spatial or temporal characteristics of the intellectual content.
    """


class CoverageType(PBCoreElement):
    """CoverageType element.
    
    Definition: The coverageType element specifies whether the coverage is spatial or temporal.
    """


class PBCoreCoverage(PBCoreBaseModel):
    """PBCoreCoverage element.
    
    Definition: The pbcoreCoverage element describes the spatial or temporal characteristics of the intellectual content.
    """

    coverage: Coverage
    coverageType: CoverageType | None = None


class PBCoreAudienceLevel(PBCoreElement):
    """PBCoreAudienceLevel element.
    
    Definition: The pbcoreAudienceLevel element is used to identify the intended audience for the content being described.
    """


class PBCoreAudienceRating(PBCoreElement):
    """PBCoreAudienceRating element.
    
    Definition: The pbcoreAudienceRating element is used to identify the intended audience rating for the content being described.
    """


class Creator(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Creator element.
    
    Definition: The creator element identifies the entity responsible for creating the intellectual content.
    """


class CreatorRole(PBCoreElement):
    """CreatorRole element.
    
    Definition: The creatorRole element identifies the role of the creator in the creation of the intellectual content.
    """


class PBCoreCreator(PBCoreBaseModel):
    """PBCoreCreator element.
    
    Definition: The pbcoreCreator element identifies the entity responsible for creating the intellectual content.
    """

    creator: Creator
    creatorRole: list[CreatorRole] | None = Field(None, min_length=1)


class Contributor(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Contributor element.
    
    Definition: The contributor element identifies entities that have contributed to the intellectual content.
    """


class ContributorRole(PBCoreElement):
    """ContributorRole element.
    
    Definition: The contributorRole element identifies the role of the contributor to the intellectual content.
    """

    portrayal: str | None = Field(None, description="The portrayal associated with the contributor role")


class PBCoreContributor(PBCoreBaseModel):
    """PBCoreContributor element.
    
    Definition: The pbcoreContributor element identifies entities that have contributed to the intellectual content.
    """

    contributor: Contributor
    contributorRole: list[ContributorRole] | None = Field(None, min_length=1)


class Publisher(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Publisher element.
    
    Definition: The publisher element identifies the entity responsible for publishing the intellectual content.
    """


class PublisherRole(PBCoreElement):
    """PublisherRole element.
    
    Definition: The publisherRole element identifies the role of the publisher for the intellectual content.
    """


class PBCorePublisher(PBCoreBaseModel):
    """PBCorePublisher element.
    
    Definition: The pbcorePublisher element identifies the entity responsible for publishing the intellectual content.
    """

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
