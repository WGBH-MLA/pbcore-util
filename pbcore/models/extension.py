from pbcore.models import PBCoreTextElement, PBCoreBaseAttributes, PBCoreBaseModel
from pydantic import Field, model_validator


class ExtensionElement(PBCoreTextElement):
    """ExtensionElement element.
    
    Definition: The extensionElement allows for the specification of a metadata element name.
    """


class ExtensionValue(PBCoreTextElement):
    """ExtensionValue element.
    
    Definition: The extensionValue allows for the specification of a metadata element value.
    """


class ExtensionAuthorityUsed(PBCoreTextElement):
    """ExtensionAuthorityUsed element.
    
    Definition: The extensionAuthorityUsed allows for the specification of the authority or controlled vocabulary used for the extension.
    """


class ExtensionWrap(PBCoreBaseAttributes):
    """ExtensionWrap element.
    
    Definition: The extensionWrap element allows for the inclusion of metadata from other metadata schemas.
    """

    extensionElement: ExtensionElement
    extensionValue: ExtensionValue
    extensionAuthorityUsed: ExtensionAuthorityUsed | None = None


class ExtensionEmbedded(PBCoreBaseAttributes):
    """ExtensionEmbedded element.
    
    Definition: The extensionEmbedded element allows for the embedding of XML from other namespaces within PBCore.
    """


class PBCoreExtension(PBCoreBaseModel):
    """PBCoreExtension element.
    
    Definition: The pbcoreExtension element allows for the inclusion of metadata from other namespaces or standards.
    """

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

    extensionWrap: list[ExtensionWrap] | None = Field(None, min_length=1)
    extensionEmbedded: list[ExtensionEmbedded] | None = Field(None, min_length=1)
