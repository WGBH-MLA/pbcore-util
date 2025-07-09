from typing import Optional

from pydantic import BaseModel


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
    """Base class for date type attributes in PBCore."""

    dateType: Optional[str] = None


class PBCoreAttributesTime(PBCoreBaseModel):
    """Base class for time attributes in PBCore."""

    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timeAnnotation: Optional[str] = None


class PBCoreAttributesAffiliation(PBCoreBaseModel):
    """Base class for affiliation attributes in PBCore."""

    affiliation: Optional[str] = None
    affiliationSource: Optional[str] = None
    affiliationRef: Optional[str] = None
    affiliationVersion: Optional[str] = None
    affiliationAnnotation: Optional[str] = None


class PBCoreElement(PBCoreTextElement, PBCoreBaseAttributes):
    """Base class for PBCore elements with required text and optional attributes."""


__all__ = [
    "PBCoreBaseModel",
    "PBCoreTextElement",
    "PBCoreBaseAttributes",
    "PBCoreAttributesDateType",
    "PBCoreAttributesTime",
    "PBCoreAttributesAffiliation",
    "PBCoreElement",
]
