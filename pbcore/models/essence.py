from pbcore.models import (
    PBCoreBaseModel,
    PBCoreElement,
    PBCoreAttributesUnits,
    PBCoreAnnotation,
)
from pbcore.models.extension import PBCoreExtension, ExtensionWrap, ExtensionEmbedded
from typing import List, Optional


class EssenceTrackType(PBCoreElement):
    """PBCore Essence Track Type element."""


class EssenceTrackIdentifier(PBCoreElement):
    """PBCore Essence Track Identifier element."""


class EssenceTrackStandard(PBCoreElement):
    """PBCore Essence Track Standard element."""


class EssenceTrackEncoding(PBCoreElement):
    """PBCore Essence Track Encoding element."""


class EssenceTrackDataRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Data Rate element."""


class EssenceTrackFrameRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Frame Rate element."""


class EssenceTrackPlaybackSpeed(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Playback Speed element."""


class EssenceTrackSamplingRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Sampling Rate element."""


class EssenceTrackBitDepth(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Bit Depth element."""


class EssenceTrackFrameSize(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Frame Size element."""


class EssenceTrackAspectRatio(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Aspect Ratio element."""


class EssenceTrackTimeStart(PBCoreElement):
    """PBCore Essence Track Time Start element."""


class EssenceTrackDuration(PBCoreElement):
    """PBCore Essence Track Duration element."""


class EssenceTrackLanguage(PBCoreElement):
    """PBCore Essence Track Language element."""


class EssenceTrackAnnotation(PBCoreAnnotation):
    """PBCore Essence Track Annotation element."""


class EssenceTrackExtension(PBCoreElement):
    """PBCore Essence Track Extension element.

    TODO: Validate that only one type of extensionWrap or extensionEmbedded is present.
    """

    extensionWrap: Optional[ExtensionWrap] = None
    extensionEmbedded: Optional[ExtensionEmbedded] = None


class InstantiationEssenceTrack(PBCoreBaseModel):
    """Instantiation of a PBCore Essence Track element."""

    essenceTrackType: EssenceTrackType
    essenceTrackAspectRatio: Optional[EssenceTrackAspectRatio] = None
