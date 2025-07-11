from pydantic import Field

from pbcore.models import (
    PBCoreAttributesTime,
    PBCoreAttributesUnits,
    PBCoreElement,
    PBCoreIdentifier,
    PBCoreAssetDate,
    PBCoreAnnotation,
)
from pbcore.models.assets import PBCoreRelationIdentifier, PBCoreRelationType
from pbcore.models.essence import (
    EssenceTrackType,
    EssenceTrackAspectRatio,
    InstantiationEssenceTrack,
)
from pbcore.models.rights import PBCoreRightsSummary


class InstantiationIdentifier(PBCoreIdentifier):
    """PBCore Instantiation Identifier element.

    Definition: The instantiationIdentifier element contains an unambiguous reference or identifier for a particular instantiation of an asset.

    Best practice: Identify the media item (whether analog or digital) by means of a string or number corresponding to an established or formal identification system if one exists. Otherwise, use an identification method that is in use within your agency, station, production company, office, or institution.
    """


class InstantiationDate(PBCoreAssetDate):
    """PBCore Instantiation Date element.

    Definition: The instantiationDate element is a date associated with an instantiation.

    Best practice: Use ISO 8601 or some other date/time standard if possible.
    """


class InstantiationDimensions(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Instantiation Dimensions element.

    Definition: The instantiationDimensions element specifies either the dimensions of a physical instantiation, or the high-level visual dimensions of a digital instantiation.

    Best practice: For physical dimensions, usage examples might be 7" for an audio reel. When describing visual dimensions, use this for high-level descriptors such as 1080p. Use the element frameSize to describe the pixel dimensions of a visual resource.
    """


class InstantiationPhysical(PBCoreElement):
    """PBCore Instantiation Physical element.

    Definition: The instantiationPhysical element is used to identify the format of a particular instantiation as it exists in a physical form that occupies physical space (e.g., a tape on a shelf). This includes physical digital media, such as a DV tape, audio CD or authored DVD, as well as analog media.

    Best practice: PBCore provides a controlled vocabulary for media objects, though any controlled vocabulary can be used as long as it is referenced. For digital storage carriers that contain portable file-based media, such as data CDs, LTO tapes or hard drives, use instantiationDigital to convey the mime type of the file instead of describing the carrier.
    """


class InstantiationDigital(PBCoreElement):
    """PBCore Instantiation Digital element.

    Definition: The instantiationDigital element is used to identify the format of a particular instantiation of an asset as it exists as a digital file on a server, hard drive, or other digital storage medium. Digital instantiations should be expressed as a formal Internet MIME types.

    Best practice: instantiationDigital should only be used to describe the MIME type of the digital file itself. There are multiple options to convey more information about the storage medium or location of the digital file, which are discussed in more detail on the PBCore site.
    """


class InstantiationStandard(PBCoreElement):
    """PBCore Instantiation Standard element.

    Definition: The instantiationStandard element + can be used, if the instantiation is a physical item, to refer to the broadcast standard of the video signal (e.g. NTSC, PAL), or the audio encoding (e.g. Dolby A, vertical cut). If the instantiation is a digital item, instantiationStandard should be used to express the container format of the digital file (e.g. MXF).

    Best practice: While the usage described in the definition is best practice for 2.1, this usage is likely to change if new elements are added for PBCore 3.0.
    """

    profile: str | None = Field(
        None, description="The profile of the instantiation standard"
    )


class InstantiationLocation(PBCoreElement):
    """PBCore Instantiation Location element.

    Definition: The instantiationLocation element may contain information about a specific location for an instantiation, such as an organization's name, departmental name, shelf ID and contact information. The instantiationLocation for a digital file should include domain, path or URI to the file.

    Best practice: For digital files, instantiationLocation should always include a path or URI to the file. There are multiple ways to convey additional information about the location of a carrier or storage medium of the digital file, which are expressed on the PBCore site.
    """


class InstantiationMediaType(PBCoreElement):
    """PBCore Instantiation Media Type element.

    Definition: The instantiationMediaType element identifies the general, high level nature of the content of an instantiation. It uses categories that show how content is presented to an observer, e.g., as a sound, text or moving image.
    """


class InstantiationGenerations(PBCoreElement):
    """PBCore Instantiation Generations element.

    Definition: The instantiationGeneration element identifies the use type and provenance of the instantiation. The generation of a video tape may be an "Original Master" or "Dub", the generation of a film reel may be an "Original Negative" or "Composite Positive", an audiotape may be a "Master" or "Mix Element", an image may be a "Photograph" or a "Photocopy.
    """


class InstantiationFileSize(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Instantiation File Size element.

    Definition: The instantiationFileSize element indicates the file size of a digital instantiation. It should contain only numerical values. As a standard, express the file size in bytes. Units of Measure should be declared in the unitsOfMeasure attribute.
    """


class InstantiationTimeStart(PBCoreElement):
    """PBCore Instantiation Time Start element.

    Definition: The instantiationTimeStart element describes the point at which playback begins for a time-based instantiation. It is likely that the content on a tape may begin an arbitrary amount of time after the beginning of the instantiation. Best practice is to use a timestamp format such as HH:MM:SS[:|;]FF or HH:MM:SS.mmm or S.mmm.
    """


class InstantiationDuration(PBCoreElement):
    """PBCore Instantiation Duration element.

    Definition: The instantiationDuration element provides a timestamp for the overall length or duration of a time-based media item. It represents the playback time. Best practice is to use a timestamp format such as HH:MM:SS[:|;]FF or HH:MM:SS.mmm or S.mmm.
    """


class InstantiationDataRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Instantiation Data Rate element.

    Definition: The instantiationDataRate element expresses the amount of data in a digital media file that is encoded, delivered or distributed, for every second of time. This should be expressed as numerical data, with the units of measure declared in the unitsOfMeasure attribute. For example, if the audio file is 56 kilobits/second, then 56 should be the value of instantiationDataRate and the attribute unitsOfMeasure should be kilobits/second.
    """


class InstantiationColors(PBCoreElement):
    """PBCore Instantiation Colors element.

    Definition: The instantiationColors element indicates the overall color, grayscale, or black and white nature of the presentation of an instantiation, as a single occurrence or combination of occurrences in or throughout the instantiation.
    """


class InstantiationTracks(PBCoreElement):
    """PBCore Instantiation Tracks element.

    Definition: The instantiationTracks element is simply intended to indicate the number and type of tracks that are found in a media item, whether it is analog or digital. (e.g. 1 video track, 2 audio tracks, 1 text track, 1 sprite track, etc.) Other configuration information specific to these identified tracks should be described using instantiationChannelConfiguration.

    Best practice: Best practices is to use essenceTracks, as this element has been deprecated.
    """


class InstantiationChannelConfiguration(PBCoreElement):
    """PBCore Instantiation Channel Configuration element.

    Definition: The instantiationChannelConfiguration element is designed to indicate, at a general narrative level, the arrangement or configuration of specific channels or layers of information within an instantiation's tracks. Examples are 2-track mono, 8- track stereo, or video track with alpha channel.
    """


class InstantiationLanguage(PBCoreElement):
    """PBCore Instantiation Language element.

    Definition: The instantiationLanguage element identifies the primary language of the tracks' audio or text. Languages must be indicated using 3-letter codes standardized in ISO 639-2 or 639-3. If an instantiation includes more than one language, the element can be repeated. Alternately, both languages can be expressed in one element by separating two three-letter codes with a semicolon, i.e. <instantiationLanguage>eng;fre</instantiationLanguage>. + Best practice: Alternative audio or text tracks and their associated languages should be identified using the element instantiationAlternativeModes.
    """


class InstantiationAlternativeModes(PBCoreElement):
    """PBCore Instantiation Alternative Modes element.

    Definition: The instantiationAlternativeModes element is a catch-all metadata element that identifies equivalent alternatives to the primary visual, sound or textual information that exists in an instantiation. These are modes that offer alternative ways to see, hear, and read the content of an instantiation. Examples include DVI (Descriptive Video Information), SAP (Supplementary Audio Program), ClosedCaptions, OpenCaptions, Subtitles, Language Dubs, and Transcripts. For each instance of available alternativeModes, the mode and its associated language should be identified together, if applicable. Examples include 'SAP in English,' 'SAP in Spanish,' 'Subtitle in French,' 'OpenCaption in Arabic.'
    """


class InstantiationAnnotation(PBCoreAnnotation):
    """PBCore Instantiation Annotation element.

    Definition: The instantiationAnnotation element is used to add any supplementary information about an instantiation of the instantiation or the metadata used to describe it. It clarifies element values, terms, descriptors, and vocabularies that may not be otherwise sufficiently understood.
    """


class InstantiationRelationType(PBCoreRelationType):
    """PBCore Instantiation Relation Type element.

    Definition: The instantiationRelationType element describes the relation between the instantiation being described and another instantiation.

    Best practice: Use to express relationships between instantiations, for example to note that they are different discrete parts of a single intellectual unit, generationally related, derivative of another, or different versions.
    """


class InstantiationRelationIdentifier(PBCoreRelationIdentifier):
    """PBCore Instantiation Relation Identifier element.

    Definition: The instantiationRelationIdentifier element is used to provide a name, locator, accession, identification number or ID where the related item can be obtained or found.

    Best practice: We recommend using a unique identifier or global unique ID in this element.
    """


class InstantiationRelation(PBCoreElement):
    """PBCore Instantiation Relation element.

    Definition: The instantiationRelation element is a container for sub-elements instantiationRelationType and instantiationRelationIdentifier to describe relationships to other instantiations.
    """

    instantiationRelationIdentifier: InstantiationRelationIdentifier
    instantiationRelationType: InstantiationRelationType


class InstantiationRights(PBCoreRightsSummary):
    """PBCore Instantiation Rights element.

    Definition: The instantiationRights element is a container for sub-elements rightsSummary, rightsLink and rightsEmbedded to describe rights particular to this instantiation."

    Best practice: This element contains rights information that is specific to an instantiation of an asset, such as rights conferred in a donation agreement that apply only to a single donated item.
    """


class PBCoreInstantiation(PBCoreAttributesTime):
    """PBCore Instantiation element.

    Definition: The pbcoreInstantiation element contains all the details on how the asset is actualized and made available for use.
    """

    instantiationIdentifier: list[InstantiationIdentifier] = Field(..., min_length=1)
    instantiationDate: list[InstantiationDate] | None = Field(None, min_length=1)
    instantiationDimensions: list[InstantiationDimensions] | None = Field(
        None, min_length=1
    )
    instantiationPhysical: InstantiationPhysical | None = None
    instantiationDigital: InstantiationDigital | None = None
    instantiationStandard: InstantiationStandard | None = None
    instantiationLocation: InstantiationLocation
    instantiationMediaType: InstantiationMediaType | None = None
    instantiationGenerations: list[InstantiationGenerations] | None = Field(
        None, min_length=1
    )
    instantiationFileSize: InstantiationFileSize | None = None
    instantiationTimeStart: list[InstantiationTimeStart] | None = Field(
        None, min_length=1
    )
    instantiationDuration: InstantiationDuration | None = None
    instantiationDataRate: InstantiationDataRate | None = None
    instantiationColors: InstantiationColors | None = None
    instantiationTracks: InstantiationTracks | None = None
    instantiationChannelConfiguration: InstantiationChannelConfiguration | None = None
    instantiationLanguage: list[InstantiationLanguage] | None = Field(
        None, min_length=1
    )
    instantiationAlternativeModes: InstantiationAlternativeModes | None = None
    instantiationEssenceTrack: list[InstantiationEssenceTrack] | None = Field(
        None, min_length=1
    )
    instantiationRelation: list[InstantiationRelation] | None = Field(
        None, min_length=1
    )
    instantiationRights: list[InstantiationRights] | None = Field(None, min_length=1)

    instantiationAnnotation: list[InstantiationAnnotation] | None = Field(
        None, min_length=1
    )


__all__ = [
    "InstantiationIdentifier",
    "InstantiationPhysical",
    "InstantiationLocation",
    "InstantiationMediaType",
    "InstantiationGenerations",
    "InstantiationDuration",
    "InstantiationTracks",
    "InstantiationChannelConfiguration",
    "InstantiationAlternativeModes",
    "EssenceTrackType",
    "EssenceTrackAspectRatio",
    "InstantiationEssenceTrack",
    "InstantiationAnnotation",
    "PBCoreInstantiation",
]
