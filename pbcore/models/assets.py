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

    Definition: The pbcoreAssetType element is a broad definition of the type of intellectual content being described. Asset types might include those without associated instantiations (a collection or series), or those with instantiations (programs, episodes, clips, etc.)"

    Best practice: The asset type should broadly describe all related instantiations -- for example, if an asset includes many instantiations representing different generations of a program, the asset type 'program' remains accurate for all of them."
    """


class PBCoreAssetDate(PBCoreElement, PBCoreAttributesDateType):
    """PBCoreAssetDate element.

    Definition: The pbcoreAssetDate element is intended to reflect dates associated with the Intellectual Content.

    Best practice: By contrast, instantiationDate is intended to reflect date information for the specific instance. For example, if you have a VHS copy of Gone With The Wind, the pbcoreAssetDate would be 1939, while the instantiationDate of the VHS copy could be 1985. pbcoreAssetDate may also be used to reflect availability dates, etc. Date types should be specified using the @dateType attribute. Dates or time-based events related to the content of the asset, on the other hand, would be described in the 'coverage' element -- so, while the storyline of Gone with the Wind takes place in the nineteenth century, this information should be noted in the Coverage field, not the assetDate field. Best practice is to use ISO 8601 or some other date/time standard if possible.
    """


class PBCoreIdentifier(PBCoreElement):
    """PBCoreIdentifier element.

    Definition: The pbcoreIdentifier element provides an identifier that can apply to the asset. This identifier should not be limited to a specific instantiation, but rather is shared by or common to all instantiations of an asset. It can also hold a URL or URI that points to the asset.

    Best practice: Identify the asset by means of a string or number corresponding to an established or formal identification system if one exists. Otherwise, use an identification method that is in use within your agency, station, production company, office, or institution.
    """

    source: str = Field(
        ...,
        description="The source attribute provides the name of the authority used to declare the value of the element. Best practice: Different elements will use the source attribute slightly differently. For example, identifier source (required) should be the name of the organization, institution, system or namespace that the identifier came from, such as \"PBS NOLA Code\" or an institutional database identifier. For other elements, this might be the name of a controlled vocabulary, namespace or authority list, such as Library of Congress Subject Headings. We recommend a consistent and human readable use.",
    )


class PBCoreTitle(PBCoreElement, PBCoreAttributesTime):
    """PBCoreTitle element.

    Definition: The pbcoreTitle element is a name or label relevant to the asset.

    Best practice: An asset may have many types of titles, an asset may have, such as a series title, episode title, segment title, or project title; therefore the element is repeatable.
    """

    titleType: str | None = Field(
        None,
        description="The titleType attribute is used to indicate the type of title being assigned to the asset, such as series title, episode title or project title.",
    )
    titleTypeSource: str | None = Field(
        None,
        description="The titleTypeSource attribute is used to provides the name of the authority used to declare data value of the titleType attribute. Best practice: This might be the name of a controlled vocabulary, namespace or authority list, such as the official PBCore vocabulary. We recommend a consistent and human readable use.",
    )
    titleTypeRef: str | None = Field(
        None,
        description="The titleTypeRef attribute is used to supply a source's URI for the value of the attribute titleTypeSource. Best practice: Attribute titleTypeRef can be used to point to a term in a controlled vocabulary, or a URI associated with a source.",
    )
    titleTypeVersion: str | None = Field(
        None,
        description="The titleTypeVersion attribute identifies any version information about the authority or convention used to express data of this element.",
    )
    titleTypeAnnotation: str | None = Field(
        None,
        description="The titleTypeAnnotation attribute includes narrative information intended to clarify the nature of data used in the element.",
    )


class PBCoreSubject(PBCoreElement, PBCoreAttributesTime):
    """PBCoreSubject element.

    Definition: The pbcoreSubject element is used to assign topic headings or keywords that portray the intellectual content of the asset. A subject is expressed by keywords, key phrases, or even specific classification codes. Controlled vocabularies, authorities, formal classification codes, as well as folksonomies and user-generated tags, may be employed when assigning descriptive subject terms.
    """

    subjectType: str | None = Field(
        None,
        description="The subjectType attribute is used to indicate the type of subject being assigned to the attribute subjectType, such as 'topic,' 'personal name,' or 'keyword'.",
    )
    subjectTypeSource: str | None = Field(
        None,
        description="The subjectTypeSource attribute provides the name of the authority used to declare the value of the attribute subjectType. Best practice: This might be the name of a controlled vocabulary, namespace or authority list, such as the official PBCore vocabulary. We recommend a consistent and human readable use.",
    )
    subjectTypeRef: str | None = Field(
        None,
        description="The subjectTypeRef attribute is used to supply a source's URI for the value of the attribute subjectType. Best practice: Attribute subjectTypeRef can be used to point to a term in a controlled vocabulary, or a URI associated with a source.",
    )
    subjectTypeVersion: str | None = Field(
        None,
        description="The subjectTypeVersion attribute identifies any version information about the authority or convention used to express data of the attribute subjectType.",
    )
    subjectTypeAnnotation: str | None = Field(
        None,
        description="The subjectTypeAnnotation attribute includes narrative information intended to clarify the nature of data used in the attribute subjectType. Best practice: This attribute can be used as a notes field to include any additional information about the element or associated attributes.",
    )


class PBCoreDescription(PBCoreElement, PBCoreAttributesTime):
    """PBCoreDescription element.

    Definition: The pbcoreDescription element uses free-form text or a narrative to report general notes, abstracts, or summaries about the intellectual content of an asset. The information may be in the form of an individual program description, anecdotal interpretations, or brief content reviews. The description may also consist of outlines, lists, bullet points, rundowns, edit decision lists, indexes, or tables of content.
    """

    descriptionType: str | None = Field(
        None,
        description="The descriptionType attribute is used to indicate the type of description being assigned to the element, such as 'abstract,' 'summary,' or 'physical description.'",
    )
    descriptionTypeSource: str | None = Field(
        None,
        description="The descriptionTypeSource attribute provides the name of the authority used to declare data value of the attribute descriptionType. Best practice: This might be the name of a controlled vocabulary, namespace or authority list, such as the official PBCore recommended vocabulary. We recommend a consistent and human readable use.",
    )
    descriptionTypeRef: str | None = Field(
        None,
        description="The descriptionTypeRef attribute is used to supply a source's URI for the value of the attribute descriptionType. Best practice: The descriptionTypeRef attribute can be used to point to a term in a controlled vocabulary, or a URI associated with a source.",
    )
    descriptionTypeVersion: str | None = Field(
        None,
        description="The descriptionTypeVersion attribute identifies any version information about the authority or convention used to express data of the attribute descriptionType.",
    )
    descriptionTypeAnnotation: str | None = Field(
        None,
        description="The descriptionTypeAnnotation attribute includes narrative information intended to clarify the nature of data used in the element. Best practice: This attribute can be used as a notes field to include any additional information about the element or associated attributes.",
    )

    segmentType: str | None = Field(
        None,
        description="The segmentType attribute is used to define the type of content contained in a segment. Best practice: We recommend using description and descriptionType instead of segmentType.'",
    )
    segmentTypeSource: str | None = Field(
        None,
        description="The segmentTypeSource attribute provides the name of the authority used to declare data value of the attribute segmentType. Best practice: This might be the name of a controlled vocabulary, namespace or authority list, such as the official PBCore recommended vocabulary.",
    )
    segmentTypeRef: str | None = Field(
        None,
        description="The segmentTypeRef attribute is used to supply a source's URI for the value of the attribute segmentType. Best practice: Attribute segmentTypeRef can be used to point to a term in a controlled vocabulary, or a URI associated with a source.",
    )
    segmentTypeVersion: str | None = Field(
        None,
        description="The segmentTypeVersion attribute identifies any version information about the authority or convention used to express data of the attribute segmentType.",
    )
    segmentTypeAnnotation: str | None = Field(
        None,
        description="The segmentTypeAnnotation attribute includes narrative information intended to clarify the nature of data used in the attribute segmentType. Best practice: This attribute can be used as a notes field to include any additional information about the element or associated attributes.",
    )


class PBCoreGenre(PBCoreElement, PBCoreAttributesTime):
    """PBCore Genre element.

    Definition: The pbcoreGenre element describes the Genre of the asset, which can be defined as a categorical description informed by the topical nature or a particular style or form of the content.

    Best practice: Genre refers to the intellectual content of the asset, whereas the element pbcoreAssetType defines a broader structural category; i.e. an asset might have the Asset Type of Segment, with a Genre of News, together defining a news segment.
    """


class PBCoreRelationType(PBCoreElement):
    """PBCoreRelationType element.

    Definition: The pbcoreRelationType element describes the relationship between the asset being describe by the pbcore document and any other asset. Ideally it would contain text from a controlled vocabulary for describing relationships. There is some depth to what a relationship could be. The assets can be related as different episodes in a series, different tapes in a box set, or different versions of an original, among others.

    Best practice: The assets may be related in that they are different discrete parts of a single intellectual unit, one may be a derivative of another, or they may be different versions that are distinct enough to be described as separate assets.
    """


class PBCoreRelationIdentifier(PBCoreElement):
    """PBCoreRelationIdentifier element.

    Definition: The pbcoreRelationIdentifier element contains the identifier of the related asset. In the case that the related asset has a PBCore record, this identifier should correspond with the pbcoreIdentifier of the related asset. However, it is possible to use this element with a record that isn't in PBCore, in which case the source attribute should identify the source of the identifier.
    """


class PBCoreRelation(PBCoreBaseModel):
    """PBCore Relation element.

    Definition: The pbcoreRelation element contains the pbcoreRelationType and pbcoreRelationIdentifier elements. In order to properly use these two elements they must be nested with the pbcoreRelation element, and pbcoreRelation must contain both pbcoreRelationType and pbcoreRelationIdentifier if it is included.
    """

    pbcoreRelationType: PBCoreRelationType
    pbcoreRelationIdentifier: PBCoreRelationIdentifier


class Coverage(PBCoreElement, PBCoreAttributesTime):
    """Coverage element.

    Definition: The coverage element refers to either the geographic location or the time period covered by the asset's intellectual content. For geographic locations ('spatial' descriptors), it is expressed by keywords such as place names (e.g. 'Alaska' or 'Washington, DC'), numeric coordinates or geo-spatial data. For time-based events ('temporal' descriptors), it is expressed by using a date, period, era, or time-based event that is portrayed or covered in the intellectual content (e.g. '2007' or 'Victorian Era'). The PBCore metadata element coverage houses the actual spatial or temporal keywords. The companion element coverageType is used to identify the type of keywords that are being used.
    """


class CoverageType(PBCoreElement):
    """CoverageType element.

    Definition: The coverageType element is used to identify the actual type of keywords that are being used by its companion metadata element coverage. coverageType provides a picklist of two possible types - spatial or temporal - because coverage in intellectual content may be expressed spatially by geographic location or it may also be expressed temporally by a date, period, era, or time-based event."
    """


class PBCoreCoverage(PBCoreBaseModel):
    """PBCoreCoverage element.

    Definition: The pbcoreCoverage element is a container for sub-elements 'coverage' and 'coverageType'.
    """

    coverage: Coverage
    coverageType: CoverageType | None = None


class PBCoreAudienceLevel(PBCoreElement):
    """PBCoreAudienceLevel element.

    Definition: The pbcoreAudienceLevel element identifies a type of audience, viewer, or listener for whom the media item is primarily designed or educationally useful.
    """


class PBCoreAudienceRating(PBCoreElement):
    """PBCoreAudienceRating element.

    Definition: The pbcoreAudienceRating element designates the type of users for whom the intellectual content of a media item is intended or judged appropriate. This element differs from the element pbcoreAudienceLevel in that it utilizes standard ratings that have been crafted by the broadcast television and film industries and that are used as flags for audience or age-appropriate materials.
    """


class Creator(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Creator element.

    Definition: The creator element identifies the primary person, people, or organization(s) responsible for creating the asset. Note that non-primary names and roles should be included within the pbcoreContributor container. Best practice: We recommend providing a consistent internal standard for entering proper names and organizational names, such as 'Last name, First name, Middle name,' or 'Main group, subdivision.' We also recommend supplying separate pbcoreCreator containers for each creator to be named for a resource.
    """


class CreatorRole(PBCoreElement):
    """CreatorRole element.

    Definition: The creatorRole element is used to identify the role played by the person, people or organization(s) identified in the companion descriptor creator. The PBCore schema allows for creatorRole to be repeated in the pbcoreCreator container element. This can be useful when a single person or organization is associated with multiple roles in an asset.
    """


class PBCoreCreator(PBCoreBaseModel):
    """PBCoreCreator element.

    Definition: The pbcoreCreator element is a container for sub-elements 'creator' and 'creatorRole'.
    """

    creator: Creator
    creatorRole: list[CreatorRole] | None = Field(None, min_length=1)


class Contributor(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Contributor element.

    Definition: The contributor element identifies a person, people, or organization that has made substantial creative contributions to the asset. This contribution is considered to be secondary to the primary author(s) (person or organization) identified in the descriptor creator. Best practice: We recommend providing a consistent internal standard for entering proper names and organizational names, such as 'Last name, First name, Middle name,' or 'Main group, subdivision.' We also recommend supplying separate pbcoreCreator containers for each creator to be named for a resource.
    """


class ContributorRole(PBCoreElement):
    """ContributorRole element.

    Definition: The contributorRole element is used to identify the role played by the person, people or organizations identified in the companion element contributor. The PBCore schema allows for contributorRole to be repeated in the pbcoreContributor container element. This can be useful when a single person or organization is associated with multiple roles in an asset.
    """

    portrayal: str | None = Field(
        None,
        description="The portrayal attribute identifies any roles or characters performed by a contributor.",
    )


class PBCoreContributor(PBCoreBaseModel):
    """PBCoreContributor element.

    Definition: The pbcoreContributor element is a container for sub-elements 'contributor' and 'contributorRole'.
    """

    contributor: Contributor
    contributorRole: list[ContributorRole] | None = Field(None, min_length=1)


class Publisher(PBCoreElement, PBCoreAttributesAffiliation, PBCoreAttributesTime):
    """Publisher element.

    Definition: The publisher element identifies a person, people, or organization primarily responsible for distributing or making the asset available to others. The publisher may be a person, a business, organization, group, project or service. Best practice: We recommend providing a consistent internal standard for entering proper names and organizational names, such as 'Last name, First name, Middle name,' or 'Main group, subdivision.' We also recommend supplying separate pbcoreCreator containers for each creator to be named for a resource.
    """


class PublisherRole(PBCoreElement):
    """PublisherRole element.

    Definition: The publisherRole element is used to identify the role played by the specific publisher or publishing entity identified in the companion descriptor publisher. The PBCore schema allows for publisherRole to be repeated in the pbcorePublisher container element. This can be useful when a single person or organization is associated with multiple roles in an asset.
    """


class PBCorePublisher(PBCoreBaseModel):
    """PBCorePublisher element.

    Definition: The pbcorePublisher element is a container for sub-elements 'publisher' and 'publisherRole.'
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
