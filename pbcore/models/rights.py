from typing import Optional
from pydantic import Field, model_validator
from pbcore.models.base import (
    PBCoreElement,
    PBCoreAttributesTime,
)


class RightsSummary(PBCoreElement):
    """RightsSummary element."""


class RightsLink(PBCoreElement):
    """RightsLink element."""


class RightsEmbedded(PBCoreElement):
    """RightsEmbedded element."""


class PBCoreRightsSummary(PBCoreAttributesTime):
    """PBCoreRightsSummary element."""

    @model_validator(mode='after')
    def validate_rights(cls, values):
        types = 0
        if values.rightsSummary:
            types += 1
        if values.rightsLink:
            types += 1
        if values.rightsEmbedded:
            types += 1
        if types == 0:
            raise ValueError(
                'At least one of rightsSummary, rightsLink, or rightsEmbedded must be present.'
            )
        if types > 1:
            raise ValueError(
                'Only one of rightsSummary, rightsLink, or rightsEmbedded may be present.'
            )
        return values

    rightsSummary: Optional[list[RightsSummary]] = Field(None, min_length=1)
    rightsLink: Optional[list[RightsLink]] = Field(None, min_length=1)
    rightsEmbedded: Optional[list[RightsEmbedded]] = Field(None, min_length=1)
