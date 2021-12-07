from enum import Enum, auto


class Facility:
    def __init__(self, name: str, efficiency: float, power_kwh: float):
        self.name = name
        self.efficiency = efficiency
        self.power_kwh = power_kwh


class FacilityType(Enum):
    miner = auto()
    smelter = auto()
    assembler = auto()
    water_pump = auto()
    oil_extractor = auto()
    oil_refinery = auto()
    fractionator = auto()
    chemical = auto()
    particle_collider = auto()
    research_facility = auto()


facilities = {
    FacilityType.miner: [Facility("Mining machine", 33, 420)],
    FacilityType.smelter: [
        Facility("Arc smelter", 1, 360),
        Facility("Plane smelter", 2, 1440),
    ],
    FacilityType.assembler: [
        Facility("Assembling machine Mk.I", 0.75, 270),
        Facility("Assembling machine Mk.II", 1, 540),
        Facility("Assembling machine Mk.III", 1.5, 1080),
    ],
    FacilityType.water_pump: [Facility("Water pump", 55, 300)],
    FacilityType.oil_extractor: [Facility("Oil extractor", 1.1, 840)],
    FacilityType.oil_refinery: [Facility("Oil refinery", 1, 960)],
    FacilityType.fractionator: [Facility("Fractionator", 1, 720)],
    FacilityType.chemical: [Facility("Chemical plant", 1, 720)],
    FacilityType.particle_collider: [Facility("Miniature particle collider", 1, 12000)],
    FacilityType.research_facility: [Facility("Research facility", 1, 480)],
}
