from pydantic import BaseModel, Field


# Base classes for PBCore elements


class PBCoreBaseModel(BaseModel):
    """Base class for all PBCore elements."""


class PBCoreTextElement(PBCoreBaseModel):
    """Base class for a required text elements in PBCore."""

    text: str


class PBCoreBaseAttributes(PBCoreBaseModel):
    """Base class for attributes in PBCore.

    Definition: The grouping of attributes: source, ref, version, annotation that are common across many PBCore elements.
    """

    source: str | None = Field(
        None,
        description="The source attribute identifies the authority, standard, or particular controlled vocabulary used when populating an element",
    )
    ref: str | None = Field(
        None, description="The ref attribute provides a URI that relates to the element"
    )
    version: str | None = Field(
        None,
        description="The version attribute identifies the version of the authority, standard, or particular controlled vocabulary",
    )
    annotation: str | None = Field(
        None,
        description="The annotation attribute provides additional information about the element",
    )


class PBCoreAttributesDateType(PBCoreBaseModel):
    """Base class for date type attributes in PBCore."""

    dateType: str | None = Field(None, description="The type of date being represented")


class PBCoreAttributesTime(PBCoreBaseModel):
    """Base class for time attributes in PBCore.

    Definition: The grouping of attributes: startTime, endTime, timeAnnotation for time-based annotations.
    """

    startTime: str | None = Field(None, description="The start time for the element")
    endTime: str | None = Field(None, description="The end time for the element")
    timeAnnotation: str | None = Field(
        None, description="Additional information about the time annotation"
    )


class PBCoreAttributesAffiliation(PBCoreBaseModel):
    """Base class for affiliation attributes in PBCore."""

    affiliation: str | None = Field(
        None, description="The affiliation associated with the element"
    )
    affiliationSource: str | None = Field(
        None, description="The source of the affiliation"
    )
    affiliationRef: str | None = Field(
        None, description="Reference URI for the affiliation"
    )
    affiliationVersion: str | None = Field(
        None, description="Version of the affiliation"
    )
    affiliationAnnotation: str | None = Field(
        None, description="Annotation for the affiliation"
    )


class PBCoreAttributesUnits(PBCoreBaseModel):
    """Base class for units of measure attributes in PBCore."""

    unitsOfMeasure: str | None = Field(
        None, description="The units of measure for the element value"
    )


class PBCoreElement(PBCoreTextElement, PBCoreBaseAttributes):
    """Base class for PBCore elements with required text and optional attributes."""


class PBCoreAnnotation(PBCoreElement):
    """PBCoreAnnotation element.

    Definition: The pbcoreAnnotation element allows the addition of any supplementary information about the metadata used to describe the PBCore record. pbcoreAnnotation clarifies element values, terms, descriptors, and vocabularies that may not be otherwise sufficiently understood.
    """

    annotationType: str | None = Field(None, description="The type of annotation")


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
