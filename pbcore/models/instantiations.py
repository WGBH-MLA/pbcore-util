from typing import List, Optional

from pbcore.models import (
    PBCoreAttributesTime,
    PBCoreAttributesUnits,
    PBCoreBaseModel,
    PBCoreElement,
    PBCoreIdentifier,
    PBCoreAssetDate,
)
from pbcore.models.essence import (
    EssenceTrackType,
    EssenceTrackAspectRatio,
    InstantiationEssenceTrack,
)


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

    profile: Optional[str] = None


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


class InstantiationAnnotation(PBCoreBaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreInstantiation(PBCoreAttributesTime):
    instantiationIdentifier: List[InstantiationIdentifier]
    instantiationPhysical: Optional[InstantiationPhysical] = None
    instantiationLocation: InstantiationLocation
    instantiationMediaType: Optional[InstantiationMediaType] = None
    instantiationGenerations: Optional[List[InstantiationGenerations]] = None
    instantiationDuration: Optional[InstantiationDuration] = None
    instantiationTracks: Optional[InstantiationTracks] = None
    instantiationChannelConfiguration: Optional[InstantiationChannelConfiguration] = (
        None
    )
    instantiationAlternativeModes: Optional[InstantiationAlternativeModes] = None
    instantiationEssenceTrack: Optional[List[InstantiationEssenceTrack]] = None
    instantiationAnnotation: Optional[List[InstantiationAnnotation]] = None


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
