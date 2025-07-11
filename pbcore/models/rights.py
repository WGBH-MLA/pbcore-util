from pydantic import Field, model_validator
from pbcore.models.base import (
    PBCoreElement,
    PBCoreAttributesTime,
)


class RightsSummary(PBCoreElement):
    """RightsSummary element.
    
    Definition: The rightsSummary element allows for a free-text description of rights held in and over the media item.
    """


class RightsLink(PBCoreElement):
    """RightsLink element.
    
    Definition: The rightsLink element allows for the use of a URI that links to rights information for the media item.
    """


class RightsEmbedded(PBCoreElement):
    """RightsEmbedded element.
    
    Definition: The rightsEmbedded element allows for the embedding of other rights schemas within PBCore.
    """


class PBCoreRightsSummary(PBCoreAttributesTime):
    """PBCoreRightsSummary element.
    
    Definition: The pbcoreRightsSummary element allows for the expression of rights information for the media item.
    """

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
