from typing import List, Optional
from pbcore.models import PBCoreTextElement, PBCoreBaseAttributes, PBCoreBaseModel
from pydantic import Field


class ExtensionElement(PBCoreTextElement):
    """ExtensionElement element."""


class ExtensionValue(PBCoreTextElement):
    """ExtensionValue element."""


class ExtensionAuthorityUsed(PBCoreTextElement):
    """ExtensionAuthorityUsed element."""


class ExtensionWrap(PBCoreBaseAttributes):
    """ExtensionWrap element."""

    extensionElement: ExtensionElement
    extensionValue: ExtensionValue
    extensionAuthorityUsed: Optional[ExtensionAuthorityUsed] = None


class ExtensionEmbedded(PBCoreBaseAttributes):
    """ExtensionEmbedded element."""


class PBCoreExtension(PBCoreBaseModel):
    """PBCoreExtension element.

    TODO: Validate that extensionWrap and extensionEmbedded are not both present."""

    extensionWrap: Optional[List[ExtensionWrap]] = Field(None, min_length=1)
    extensionEmbedded: Optional[List[ExtensionEmbedded]] = Field(None, min_length=1)
