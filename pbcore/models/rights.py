from typing import List, Optional
from pydantic import Field
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
    """PBCoreRightsSummary element.

    TODO: Validate that only one type of rightsSummary, rightsLink, or rightsEmbedded are present.
    """

    rightsSummary: Optional[List[RightsSummary]] = Field(None, min_length=1)
    rightsLink: Optional[List[RightsLink]] = Field(None, min_length=1)
    rightsEmbedded: Optional[List[RightsEmbedded]] = Field(None, min_length=1)
