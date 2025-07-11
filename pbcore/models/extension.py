from pbcore.models import PBCoreTextElement, PBCoreBaseAttributes, PBCoreBaseModel
from pydantic import Field, model_validator


class ExtensionElement(PBCoreTextElement):
    """ExtensionElement element.

    Definition: The extensionElement element should contain the name of an element used from another metadata standard, in the case that an element from another + metadata standard is used. While we recommend the usage of an existing standard, this element can also be used to define local elements that may not be part of an existing standard."

    Best practice: These extensions fulfill the metadata requirements for communities identifying and describing their own types of media with specialized, custom terminologies.
    """


class ExtensionValue(PBCoreTextElement):
    """ExtensionValue element.

    Definition: The extensionValue element is used to express the data value of the label indicated by extensionElement.
    """


class ExtensionAuthorityUsed(PBCoreTextElement):
    """ExtensionAuthorityUsed element.

    Definition: The extensionAuthorityUsed element identifies the authority used for the extensionElement.

    Best practice: If metadata extensions to PBCore are assigned to a media item with the element extensionElement, and the terms used are derived from a specific authority or metadata scheme, use extensionAuthorityUsed to identify whose metadata extensions are being used.
    """


class ExtensionWrap(PBCoreBaseAttributes):
    """ExtensionWrap element.

    Definition: The extensionWrap element serves as a container for the elements extensionElement, extensionValue, and extensionAuthorityUsed.
    """

    extensionElement: ExtensionElement
    extensionValue: ExtensionValue
    extensionAuthorityUsed: ExtensionAuthorityUsed | None = None


class ExtensionEmbedded(PBCoreBaseAttributes):
    """ExtensionEmbedded element.

    Definition: The extensionEmbedded element allows the inclusion of xml from another schema, e.g. TEI, METS, etc.
    """


class PBCoreExtension(PBCoreBaseModel):
    """PBCoreExtension element.

    Definition: The pbcoreExtension element can be used as either a wrapper containing a specific element from another standard OR embedded xml containing the extension.

    Best practice: Use it to supplement other metadata sub-elements of the PBCore description document in which it appears.
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
