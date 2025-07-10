from typing import Optional
from pbcore.models import PBCoreTextElement, PBCoreBaseAttributes, PBCoreBaseModel
from pydantic import Field, model_validator


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
    """PBCoreExtension element."""

    @model_validator(mode='after')
    def validate_extensions(self):
        """Ensure exclusively one of extensionWrap or extensionEmbedded is provided"""
        if self.extensionWrap and self.extensionEmbedded:
            raise ValueError(
                "PBCoreExtension can have either extensionWrap or extensionEmbedded, not both."
            )
        if not self.extensionWrap and not self.extensionEmbedded:
            raise ValueError(
                "PBCoreExtension must have either extensionWrap or extensionEmbedded."
            )
        return self

    extensionWrap: Optional[list[ExtensionWrap]] = Field(None, min_length=1)
    extensionEmbedded: Optional[list[ExtensionEmbedded]] = Field(None, min_length=1)
