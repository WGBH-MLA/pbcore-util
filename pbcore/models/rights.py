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
    def validate_rights(self):
        types = 0
        if self.rightsSummary:
            types += 1
        if self.rightsLink:
            types += 1
        if self.rightsEmbedded:
            types += 1
        if types > 1:
            raise ValueError(
                'Only one of rightsSummary, rightsLink, or rightsEmbedded may be present.'
            )
        return self

    rightsSummary: list[RightsSummary] | None = Field(None, min_length=1)
    rightsLink: list[RightsLink] | None = Field(None, min_length=1)
    rightsEmbedded: list[RightsEmbedded] | None = Field(None, min_length=1)
