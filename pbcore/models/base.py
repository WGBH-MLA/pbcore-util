from pydantic import BaseModel


# Base classes for PBCore elements


class PBCoreBaseModel(BaseModel):
    """Base class for all PBCore elements."""


class PBCoreTextElement(PBCoreBaseModel):
    """Base class for a required text elements in PBCore."""

    text: str


class PBCoreBaseAttributes(PBCoreBaseModel):
    """Base class for attributes in PBCore."""

    source: str | None = None
    ref: str | None = None
    version: str | None = None
    annotation: str | None = None


class PBCoreAttributesDateType(PBCoreBaseModel):
    """Base class for date type attributes in PBCore."""

    dateType: str | None = None


class PBCoreAttributesTime(PBCoreBaseModel):
    """Base class for time attributes in PBCore."""

    startTime: str | None = None
    endTime: str | None = None
    timeAnnotation: str | None = None


class PBCoreAttributesAffiliation(PBCoreBaseModel):
    """Base class for affiliation attributes in PBCore."""

    affiliation: str | None = None
    affiliationSource: str | None = None
    affiliationRef: str | None = None
    affiliationVersion: str | None = None
    affiliationAnnotation: str | None = None


class PBCoreAttributesUnits(PBCoreBaseModel):
    """Base class for units of measure attributes in PBCore."""

    unitsOfMeasure: str | None = None


class PBCoreElement(PBCoreTextElement, PBCoreBaseAttributes):
    """Base class for PBCore elements with required text and optional attributes."""


class PBCoreAnnotation(PBCoreElement):
    """PBCoreAnnotation element."""

    annotationType: str | None = None


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
