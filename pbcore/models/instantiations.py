from typing import List, Optional

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
    instantiationIdentifier: List[InstantiationIdentifier] = Field(..., min_length=1)
    instantiationDate: Optional[List[InstantiationDate]] = Field(None, min_length=1)
    instantiationDimensions: Optional[List[InstantiationDimensions]] = Field(
        None, min_length=1
    )
    instantiationPhysical: Optional[InstantiationPhysical] = None
    instantiationDigital: Optional[InstantiationDigital] = None
    instantiationStandard: Optional[InstantiationStandard] = None
    instantiationLocation: InstantiationLocation
    instantiationMediaType: Optional[InstantiationMediaType] = None
    instantiationGenerations: Optional[List[InstantiationGenerations]] = Field(
        None, min_length=1
    )
    instantiationFileSize: Optional[InstantiationFileSize] = None
    instantiationTimeStart: Optional[List[InstantiationTimeStart]] = Field(
        None, min_length=1
    )
    instantiationDuration: Optional[InstantiationDuration] = None
    instantiationDataRate: Optional[InstantiationDataRate] = None
    instantiationColors: Optional[InstantiationColors] = None
    instantiationTracks: Optional[InstantiationTracks] = None
    instantiationChannelConfiguration: Optional[InstantiationChannelConfiguration] = (
        None
    )
    instantiationLanguage: Optional[List[InstantiationLanguage]] = Field(
        None, min_length=1
    )
    instantiationAlternativeModes: Optional[InstantiationAlternativeModes] = None
    instantiationEssenceTrack: Optional[List[InstantiationEssenceTrack]] = Field(
        None, min_length=1
    )
    instantiationRelation: Optional[List[InstantiationRelation]] = Field(
        None, min_length=1
    )
    instantiationRights: Optional[List[InstantiationRights]] = Field(None, min_length=1)

    instantiationAnnotation: Optional[List[InstantiationAnnotation]] = Field(
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
