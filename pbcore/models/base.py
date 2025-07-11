from pydantic import BaseModel, Field


# Base classes for PBCore elements


class PBCoreBaseModel(BaseModel):
    """Base class for all PBCore elements."""


class PBCoreTextElement(PBCoreBaseModel):
    """Base class for a required text elements in PBCore."""

    text: str


class PBCoreBaseAttributes(PBCoreBaseModel):
    """Base class for attributes in PBCore.

    Definition: The grouping of attributes: source, reference, version and annotation.
    """

    source: str | None = Field(
        None,
        description="The source attribute provides the name of the authority used to declare the value of the element. Best practice: Different elements will use the source attribute slightly differently. For example, identifier source (required) should be the name of the organization, institution, system or namespace that the identifier came from, such as \"PBS NOLA Code\" or an institutional database identifier. For other elements, this might be the name of a controlled vocabulary, namespace or authority list, such as Library of Congress Subject Headings. We recommend a consistent and human readable use.",
    )
    ref: str | None = Field(
        None,
        description="The ref attribute is used to supply a source's URI for the value of the element. Best practice: Attribute ref can be used to point to a term in a controlled vocabulary, or a URI associated with a source.",
    )
    version: str | None = Field(
        None,
        description="The version attribute identifies any version information about the authority or convention used to express data of this element.",
    )
    annotation: str | None = Field(
        None,
        description="The annotation attribute includes narrative information intended to clarify the nature of data used in the element. Best practice: This attribute can be used as a notes field to include any additional information about the element or associated attributes.",
    )


class PBCoreAttributesDateType(PBCoreBaseModel):
    """Base class for date type attributes in PBCore."""

    dateType: str | None = Field(
        None,
        description="The dateType attribute classifies by named type the date-related data of the element e.g., created, broadcast, dateAvailableStart. Best practice: Used to clarify how the date is related to the asset or instantiation. Date Created may be the most common, but the element could also be used to describe the Date Accessioned or Date Deaccessioned, for example.",
    )


class PBCoreAttributesTime(PBCoreBaseModel):
    """Base class for time attributes in PBCore.

    Definition: The grouping of attributes: startTime, endTime and timeAnnotation.
    """

    startTime: str | None = Field(
        None,
        description="The startTime attribute combines with the endTime attribute to define a specific media segment within a broader timeline of an asset and/or instantiation. Best practice: This is a free text attribute and can be applied at the asset or instantiation level. When used at the asset level, it may be used to talk generally about the start/end time of a segment (e.g. \"30 minutes\"), or by providing a timestamp to a specific point in an instantiation. If you're doing that for element at the asset level, we suggest referencing the instantiation ID you are referring to in timeAnnotation. One example would be if a six-hour long tape was broken into multiple programs, and each instantiation might have its start time labeled as when the instantiation began in the timeline of the broader tape. Another example for this usage might be a digital file created from a VHS tape that contains multiple segments. In the digital copy, color bars are removed from the beginning, and black from the end of the digital instantiation. Time references referring to the segments on the physical VHS are no longer relevant; therefore it's important to tie start and end time references to a specific instantiation, e.g. use the asset ID and timestamp.",
    )
    endTime: str | None = Field(
        None,
        description="The endTime attribute combines with a similar value in the startTime attribute to define a specific media segment within a broader timeline of an asset and/or instantiation.",
    )
    timeAnnotation: str | None = Field(
        None,
        description="The timeAnnotation attribute includes narrative information intended to clarify any time-oriented nature of data used in the element.",
    )


class PBCoreAttributesAffiliation(PBCoreBaseModel):
    """Base class for affiliation attributes in PBCore."""

    affiliation: str | None = Field(
        None,
        description="The affiliation attribute is used to indicate the organization with which an agent is associated or affiliated.",
    )
    affiliationSource: str | None = Field(
        None,
        description="The affiliationSource attribute provides the name of the authority used to declare the value of the attribute affiliation. Best practice: This might be the name of a controlled vocabulary, namespace or authority list, such as the official PBCore recommended vocabulary.",
    )
    affiliationRef: str | None = Field(
        None,
        description="The affilationRef attribute is used to supply a source's URI for the value of the attribute affiliation. Best practice: Attribute affiliationRef can be used to point to a term in a controlled vocabulary, or a URI associated with a source.",
    )
    affiliationVersion: str | None = Field(
        None,
        description="The affiliationVersion attribute identifies any version information about the authority or convention used to express data of the attribute affiliation.",
    )
    affiliationAnnotation: str | None = Field(
        None,
        description="The affiliationAnnotation attribute includes narrative information intended to clarify the nature of data used in the attribute affiliation. Best practice: This attribute can be used as a notes field to include any additional information about the element or associated attributes.",
    )


class PBCoreAttributesUnits(PBCoreBaseModel):
    """Base class for units of measure attributes in PBCore."""

    unitsOfMeasure: str | None = Field(
        None,
        description="The unitsOfMeasure attribute defines the unit used in the containing element, e.g. pixels, GB, Mb/s, ips, fps, kHz, inches, lines, dpi. Best practice: We recommend standardizing the notation that is most widely recognized in your institution and using with consistency.",
    )


class PBCoreElement(PBCoreTextElement, PBCoreBaseAttributes):
    """Base class for PBCore elements with required text and optional attributes."""


class PBCoreAnnotation(PBCoreElement):
    """PBCoreAnnotation element.

    Definition: The pbcoreAnnotation element allows the addition of any supplementary information about the metadata used to describe the PBCore record. pbcoreAnnotation clarifies element values, terms, descriptors, and vocabularies that may not be otherwise sufficiently understood.
    """

    annotationType: str | None = Field(
        None,
        description="Use the attribute annotationType to indicate the type of annotation being assigned to the asset, such as a comment, clarification, or cataloging note.",
    )


__all__ = [
    "PBCoreBaseModel",
    "PBCoreTextElement",
    "PBCoreBaseAttributes",
    "PBCoreAttributesDateType",
    "PBCoreAttributesTime",
    "PBCoreAttributesAffiliation",
    "PBCoreAttributesUnits",
    "PBCoreElement",
    "PBCoreAnnotation",
]
