from pbcore.models import (
    PBCoreBaseModel,
    PBCoreElement,
    PBCoreAttributesUnits,
    PBCoreAnnotation,
)
from pbcore.models.extension import PBCoreExtension, ExtensionWrap, ExtensionEmbedded
from pydantic import Field


class EssenceTrackType(PBCoreElement):
    """PBCore Essence Track Type element.
    
    Definition: The essenceTrackType element is used to identify the type of essence track.
    """


class EssenceTrackIdentifier(PBCoreElement):
    """PBCore Essence Track Identifier element.
    
    Definition: The essenceTrackIdentifier element is used to assign an unambiguous reference to the essence track.
    """


class EssenceTrackStandard(PBCoreElement):
    """PBCore Essence Track Standard element.
    
    Definition: The essenceTrackStandard element is used to identify the standard used for the essence track.
    """


class EssenceTrackEncoding(PBCoreElement):
    """PBCore Essence Track Encoding element.
    
    Definition: The essenceTrackEncoding element is used to identify the encoding used for the essence track.
    """


class EssenceTrackDataRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Data Rate element.
    
    Definition: The essenceTrackDataRate element is used to identify the data rate of the essence track.
    """


class EssenceTrackFrameRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Frame Rate element.
    
    Definition: The essenceTrackFrameRate element is used to identify the frame rate of the essence track.
    """


class EssenceTrackPlaybackSpeed(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Playback Speed element.
    
    Definition: The essenceTrackPlaybackSpeed element is used to identify the playback speed of the essence track.
    """


class EssenceTrackSamplingRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Sampling Rate element.
    
    Definition: The essenceTrackSamplingRate element is used to identify the sampling rate of the essence track.
    """


class EssenceTrackBitDepth(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Bit Depth element.
    
    Definition: The essenceTrackBitDepth element is used to identify the bit depth of the essence track.
    """


class EssenceTrackFrameSize(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Frame Size element.
    
    Definition: The essenceTrackFrameSize element is used to identify the frame size of the essence track.
    """


class EssenceTrackAspectRatio(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Aspect Ratio element.
    
    Definition: The essenceTrackAspectRatio element is used to identify the aspect ratio of the essence track.
    """


class EssenceTrackTimeStart(PBCoreElement):
    """PBCore Essence Track Time Start element.
    
    Definition: The essenceTrackTimeStart element is used to identify the start time of the essence track.
    """


class EssenceTrackDuration(PBCoreElement):
    """PBCore Essence Track Duration element.
    
    Definition: The essenceTrackDuration element is used to identify the duration of the essence track.
    """


class EssenceTrackLanguage(PBCoreElement):
    """PBCore Essence Track Language element.
    
    Definition: The essenceTrackLanguage element is used to identify the language of the essence track.
    """


class EssenceTrackAnnotation(PBCoreAnnotation):
    """PBCore Essence Track Annotation element.
    
    Definition: The essenceTrackAnnotation element allows for the inclusion of any type of annotation about the essence track.
    """


class EssenceTrackExtension(PBCoreExtension):
    """PBCore Essence Track Extension element.
    
    Definition: The essenceTrackExtension element allows for the inclusion of metadata from other namespaces or standards for the essence track.
    """


class InstantiationEssenceTrack(PBCoreBaseModel):
    """Instantiation of a PBCore Essence Track element.
    
    Definition: The instantiationEssenceTrack element is used to describe the technical characteristics of an essence track within an instantiation.
    """

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
