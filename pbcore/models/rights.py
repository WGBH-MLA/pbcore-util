from pydantic import Field, model_validator
from pbcore.models.base import (
    PBCoreElement,
    PBCoreAttributesTime,
)


class RightsSummary(PBCoreElement):
    """RightsSummary element.

    Definition: The rightsSummary element is used as a general free-text element to identify information about copyrights and property rights held in and over an asset or instantiation, whether they are open access or restricted in some way. If dates, times and availability periods are associated with a right, include them. End user permissions, constraints and obligations may also be identified as needed.

    Best practice: For rights information that applies to the asset as a whole, use this element within the container pbcoreRightsSummary. For rights information that is specific to an instantiation of an asset, use it within the container instantiationRights.
    """


class RightsLink(PBCoreElement):
    """RightsLink element.

    Definition: The rightsLink element is a URI pointing to a declaration of rights.
    """


class RightsEmbedded(PBCoreElement):
    """RightsEmbedded element.

    Definition: The rightsEmbedded element allows the inclusion of xml from another rights standard, e.g. ODRL, METS, etc. The included XML then defines the rights for the PBCore asset and/or PBCore instantiation.
    """


class PBCoreRightsSummary(PBCoreAttributesTime):
    """PBCoreRightsSummary element.

    Definition: Th pbcoreRightsSummary element is a container for sub-elements 'rightsSummary', 'rightsLink', and 'rightsEmbedded' used to describe Rights for the asset.
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
