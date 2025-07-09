from typing import Optional
from pbcore.models import PBCoreTextElement, PBCoreBaseAttributes, PBCoreBaseModel


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

    extensionWrap: Optional[ExtensionWrap] = None
    extensionEmbedded: Optional[ExtensionEmbedded] = None
