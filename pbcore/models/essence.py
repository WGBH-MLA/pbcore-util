from pbcore.models import (
    PBCoreBaseModel,
    PBCoreElement,
    PBCoreAttributesUnits,
    PBCoreAnnotation,
)
from pbcore.models.extension import PBCoreExtension, ExtensionWrap, ExtensionEmbedded
from pydantic import Field


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

    essenceTrackType: EssenceTrackType | None = None
    essenceTrackIdentifier: list[EssenceTrackIdentifier] | None = Field(
        None, min_length=1
    )
    essenceTrackStandard: EssenceTrackStandard | None = None
    essenceTrackEncoding: EssenceTrackEncoding | None = None
    essenceTrackDataRate: EssenceTrackDataRate | None = None
    essenceTrackFrameRate: EssenceTrackFrameRate | None = None
    essenceTrackPlaybackSpeed: EssenceTrackPlaybackSpeed | None = None
    essenceTrackSamplingRate: EssenceTrackSamplingRate | None = None
    essenceTrackBitDepth: EssenceTrackBitDepth | None = None
    essenceTrackFrameSize: EssenceTrackFrameSize | None = None
    essenceTrackAspectRatio: EssenceTrackAspectRatio | None = None
    essenceTrackTimeStart: EssenceTrackTimeStart | None = None
    essenceTrackDuration: EssenceTrackDuration | None = None
    essenceTrackLanguage: list[EssenceTrackLanguage] | None = Field(None, min_length=1)
    essenceTrackAnnotation: list[EssenceTrackAnnotation] | None = Field(
        None, min_length=1
    )
    essenceTrackExtension: list[EssenceTrackExtension] | None = Field(
        None, min_length=1
    )
