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


class EssenceTrackExtension(PBCoreExtension):
    """PBCore Essence Track Extension element."""


class InstantiationEssenceTrack(PBCoreBaseModel):
    """Instantiation of a PBCore Essence Track element."""

    essenceTrackType: Optional[EssenceTrackType] = None
    essenceTrackIdentifier: Optional[List[EssenceTrackIdentifier]] = None
    essenceTrackStandard: Optional[EssenceTrackStandard] = None
    essenceTrackEncoding: Optional[EssenceTrackEncoding] = None
    essenceTrackDataRate: Optional[EssenceTrackDataRate] = None
    essenceTrackFrameRate: Optional[EssenceTrackFrameRate] = None
    essenceTrackPlaybackSpeed: Optional[EssenceTrackPlaybackSpeed] = None
    essenceTrackSamplingRate: Optional[EssenceTrackSamplingRate] = None
    essenceTrackBitDepth: Optional[EssenceTrackBitDepth] = None
    essenceTrackFrameSize: Optional[EssenceTrackFrameSize] = None
    essenceTrackAspectRatio: Optional[EssenceTrackAspectRatio] = None
    essenceTrackTimeStart: Optional[EssenceTrackTimeStart] = None
    essenceTrackDuration: Optional[EssenceTrackDuration] = None
    essenceTrackLanguage: Optional[List[EssenceTrackLanguage]] = None
    essenceTrackAnnotation: Optional[List[EssenceTrackAnnotation]] = None
    essenceTrackExtension: Optional[List[EssenceTrackExtension]] = None
