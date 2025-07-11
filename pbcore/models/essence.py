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

    Definition: The essenceTrackType element refers to the media type of the decoded data. Tracks may possibly be of these types: video, audio, caption, metadata, image, etc.
    """


class EssenceTrackIdentifier(PBCoreElement):
    """PBCore Essence Track Identifier element.

    Definition: The essenceTrackIdentifier element is an identifier of the track. Several audiovisual containers include such identifier schema to identify each track, such as MPEG2 PIDs or QuickTime Track IDs.
    """


class EssenceTrackStandard(PBCoreElement):
    """PBCore Essence Track Standard element.

    Definition: The essenceTrackStandard element should be be used with file-based instantiations to describe the broadcast standard of the video signal (e.g. NTSC, PAL) or to further clarify the standard of the essenceTrackEncoding format.
    """


class EssenceTrackEncoding(PBCoreElement):
    """PBCore Essence Track Encoding element.

    Definition: The essenceTrackEncoding element essenceTrackEncoding identifies how the actual information in an instantiation is compressed, interpreted, or formulated using a particular scheme. Identifying the encoding used is beneficial for a number of reasons, including as a way to achieve reversible compression; for the construction of document indices to facilitate searching and access; or for efficient distribution of the information across data networks with differing bandwidths or pipeline capacities. Human-readable encoding value should be placed here. Use @ref to identify the codec ID.

    Best practice: Use @source to describe the type of encoding reference used, such as fourcc. In @ref, use a URI/URL from the source to identify the codec utilized by its container format.
    """


class EssenceTrackDataRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Data Rate element.

    Definition: The essenceTrackDataRate element measures the amount of data used per time interval for encoded data. The data rate can be calculated by dividing the total data size of the track's encoded data by a time unit. By default use bytes per second.
    """


class EssenceTrackFrameRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Frame Rate element.

    Definition: The essenceTrackFrameRate element is relevant to tracks of video track type only. The frame rate is calculated by dividing the total number of frames by the duration of the video track. By default measure frame rate in frames per second expressed as fps as a unit of measure. e.g., 24 fps.

    Best practice: Example: 1920x1080.
    """


class EssenceTrackPlaybackSpeed(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Playback Speed element.

    Definition: The essenceTrackPlaybackSpeed element specifies the rate of units against time at which the media track should be rendered for human consumption. e.g., 15ips (inches per second).
    """


class EssenceTrackSamplingRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Sampling Rate element.

    Definition: The essenceTrackSamplingRate element measures how often data is sampled when information from the audio portion from an instantiation is digitized. For a digital audio signal, the sampling rate is measured in kilohertz and is an indicator of the perceived playback quality of the media item (the higher the sampling rate, the greater the fidelity).
    """


class EssenceTrackBitDepth(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Bit Depth element.

    Definition: The essenceTrackBitDepth element specifies how much data is sampled when information is digitized, encoded, or converted for an instantiation (specifically, audio, video, or image). Bit depth is measured in bits and generally implies an arbitrary perception of quality during playback of an instantiation (the higher the bit depth, the greater the fidelity).
    """


class EssenceTrackFrameSize(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Frame Size element.

    Definition: The essenceTrackFrameSize element measures the width and height of the encoded video or image track. The frame size refers to the size of the encoded pixels and not the size of the displayed image. It may be expressed as combination of pixels measured horizontally vs. the number of pixels of image/resolution data stacked vertically (interlaced and progressive scan).
    """


class EssenceTrackAspectRatio(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Essence Track Aspect Ratio element.

    Definition: The essenceTrackAspectRatio element indicates the ratio of horizontal to vertical proportions in the display of a static image or moving image.
    """


class EssenceTrackTimeStart(PBCoreElement):
    """PBCore Essence Track Time Start element.

    Definition: The essenceTrackTimeStart element provides a time stamp for the beginning point of playback for a time-based essence track. It is likely that the content on a tape may begin an arbitrary amount of time after the beginning of the instantiation.

    Best practice: Use in combination with essenceTrackDuration to identify a sequence or segment of an essence track that has a fixed start time and end time. Best practice is to use a timestamp format such as HH:MM:SS[:|;]FF or HH:MM:SS.mmm or S.mmm.
    """


class EssenceTrackDuration(PBCoreElement):
    """PBCore Essence Track Duration element.

    Definition: The essenceTrackDuration element provides a timestamp for the overall length or duration of a track. It represents the track playback time. Best practice is to use a timestamp format such as HH:MM:SS[:|;]FF or HH:MM:SS.mmm or S.mmm.
    """


class EssenceTrackLanguage(PBCoreElement):
    """PBCore Essence Track Language element.

    Definition: The essenceTrackLanguage element identifies the primary language of the tracks' audio or text.

    Best practice: Alternative audio or text tracks and their associated languages should be identified using the element alternativeModes.
    """


class EssenceTrackAnnotation(PBCoreAnnotation):
    """PBCore Essence Track Annotation element.

    Definition: The essenceTrackAnnotation element can store any supplementary information about a track or the metadata used to describe it. It clarifies element values, terms, descriptors, and vocabularies that may not be otherwise sufficiently understood.
    """


class EssenceTrackExtension(PBCoreExtension):
    """PBCore Essence Track Extension element.

    Definition: The essenceTrackExtension element can be used as either a wrapper containing a specific element from another standard OR embedded xml containing the extension. The essenceTrackExtension element is a container to accomodate track-level metadata from external systems. Use it to supplement other metadata sub-elements of instantiationEssenceTrack in which it appears.
    """


class InstantiationEssenceTrack(PBCoreBaseModel):
    """Instantiation of a PBCore Essence Track element.

    Definition: The instantiationEssenceTrack element is an XML container element that allows for grouping of related essenceTrack elements and their repeated use. Use instantiationEssenceTrack element to describe the individual streams that comprise an instantiation, such as audio, video, timecode, etc.

    Best practice: Essence tracks can exist in either the digital or physical realm. In the digital realm, they may refer to the separate audio and video tracks within a digital file. In the physical realm, they may refer to the recorded media.
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
