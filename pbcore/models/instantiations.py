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
    """PBCore Instantiation Identifier element."""


class InstantiationDate(PBCoreAssetDate):
    """PBCore Instantiation Date element."""


class InstantiationDimensions(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Instantiation Dimensions element."""


class InstantiationPhysical(PBCoreElement):
    """PBCore Instantiation Physical element."""


class InstantiationDigital(PBCoreElement):
    """PBCore Instantiation Digital element."""


class InstantiationStandard(PBCoreElement):
    """PBCore Instantiation Standard element."""

    profile: str | None = None


class InstantiationLocation(PBCoreElement):
    """PBCore Instantiation Location element."""


class InstantiationMediaType(PBCoreElement):
    """PBCore Instantiation Media Type element."""


class InstantiationGenerations(PBCoreElement):
    """PBCore Instantiation Generations element."""


class InstantiationFileSize(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Instantiation File Size element."""


class InstantiationTimeStart(PBCoreElement):
    """PBCore Instantiation Time Start element."""


class InstantiationDuration(PBCoreElement):
    """PBCore Instantiation Duration element."""


class InstantiationDataRate(PBCoreElement, PBCoreAttributesUnits):
    """PBCore Instantiation Data Rate element."""


class InstantiationColors(PBCoreElement):
    """PBCore Instantiation Colors element."""


class InstantiationTracks(PBCoreElement):
    """PBCore Instantiation Tracks element."""


class InstantiationChannelConfiguration(PBCoreElement):
    """PBCore Instantiation Channel Configuration element."""


class InstantiationLanguage(PBCoreElement):
    """PBCore Instantiation Language element."""


class InstantiationAlternativeModes(PBCoreElement):
    """PBCore Instantiation Alternative Modes element."""


class InstantiationAnnotation(PBCoreAnnotation):
    """PBCore Instantiation Annotation element."""


class InstantiationRelationType(PBCoreRelationType):
    """PBCore Instantiation Relation Type element."""


class InstantiationRelationIdentifier(PBCoreRelationIdentifier):
    """PBCore Instantiation Relation Identifier element."""


class InstantiationRelation(PBCoreElement):
    """PBCore Instantiation Relation element."""

    instantiationRelationIdentifier: InstantiationRelationIdentifier
    instantiationRelationType: InstantiationRelationType


class InstantiationRights(PBCoreRightsSummary):
    """PBCore Instantiation Rights element."""


class PBCoreInstantiation(PBCoreAttributesTime):
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
