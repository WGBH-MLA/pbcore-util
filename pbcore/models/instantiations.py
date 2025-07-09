from typing import List, Optional

from pbcore.models.base import PBCoreBaseModel


class InstantiationIdentifier(PBCoreBaseModel):
    source: str
    text: str


class InstantiationPhysical(PBCoreBaseModel):
    text: str


class InstantiationLocation(PBCoreBaseModel):
    text: str


class InstantiationMediaType(PBCoreBaseModel):
    text: str


class InstantiationGeneration(PBCoreBaseModel):
    text: str


class InstantiationDuration(PBCoreBaseModel):
    text: str


class InstantiationTracks(PBCoreBaseModel):
    text: str


class InstantiationChannelConfiguration(PBCoreBaseModel):
    text: str


class InstantiationAlternativeModes(PBCoreBaseModel):
    text: str


class EssenceTrackType(PBCoreBaseModel):
    text: str


class EssenceTrackAspectRatio(PBCoreBaseModel):
    text: str


class InstantiationEssenceTrack(PBCoreBaseModel):
    essenceTrackType: EssenceTrackType
    essenceTrackAspectRatio: Optional[EssenceTrackAspectRatio] = None


class InstantiationAnnotation(PBCoreBaseModel):
    annotationType: Optional[str] = None
    text: str


class PBCoreInstantiation(PBCoreBaseModel):
    instantiationIdentifier: List[InstantiationIdentifier]
    instantiationPhysical: Optional[InstantiationPhysical] = None
    instantiationLocation: InstantiationLocation
    instantiationMediaType: Optional[InstantiationMediaType] = None
    instantiationGenerations: Optional[List[InstantiationGeneration]] = None
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
    "InstantiationGeneration",
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
