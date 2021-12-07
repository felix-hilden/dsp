from . import resources as r
from .base import Recipe
from .facility import FacilityType as F

# Ore / Raw material
iron_ore = Recipe(F.miner, 1, [], r.iron_ore)
copper_ore = Recipe(F.miner, 1, [], r.copper_ore)
silicon_ore = Recipe(F.miner, 1, [], r.silicon_ore)
titanium_ore = Recipe(F.miner, 1, [], r.titanium_ore)
stone = Recipe(F.miner, 1, [], r.stone)
coal = Recipe(F.miner, 1, [], r.coal)
crude_oil = Recipe(F.oil_extractor, 1, [], r.crude_oil)
water = Recipe(F.water_pump, 1, [], r.water)

# Special ore
optical_grating_crystal = Recipe(F.miner, 1, [], r.optical_grating_crystal)
fractal_silicon = Recipe(F.miner, 1, [], r.fractal_silicon)
kimberlite_ore = Recipe(F.miner, 1, [], r.kimberlite_ore)
unipolar_magnet = Recipe(F.miner, 1, [], r.unipolar_magnet)
organic_crystal_from_vein = Recipe(F.miner, 1, [], r.organic_crystal)
fire_ice = Recipe(F.miner, 1, [], r.fire_ice)
sulfuric_acid_from_lake = Recipe(F.water_pump, 1, [], r.sulfuric_acid)
spiniform_stalagmite_crystal = Recipe(F.miner, 1, [], r.spiniform_stalagmite_crystal)

# I
iron_ingot = Recipe(F.smelter, 1, r.iron_ore, r.iron_ingot)
copper_ingot = Recipe(F.smelter, 1, r.copper_ore, r.copper_ingot)
high_purity_silicon = Recipe(F.smelter, 2, 2 * r.silicon_ore, r.high_purity_silicon)
titanium_ingot = Recipe(F.smelter, 2, 2 * r.titanium_ore, r.titanium_ingot)
stone_brick = Recipe(F.smelter, 1, r.stone, r.stone_brick)
energetic_graphite = Recipe(F.smelter, 2, 2 * r.coal, r.energetic_graphite)
plasma_refining = Recipe(
    F.oil_refinery, 4, 2 * r.crude_oil, r.hydrogen + 2 * r.refined_oil
)
plastic = Recipe(F.chemical, 3, 2 * r.refined_oil + r.energetic_graphite, r.plastic)
graphene = Recipe(
    F.chemical, 3, 3 * r.energetic_graphite + r.sulfuric_acid, 2 * r.graphene
)

# II
magnet = Recipe(F.smelter, 1.5, r.iron_ore, r.magnet)
magnetic_coil = Recipe(
    F.assembler, 1, 2 * r.magnet + r.copper_ingot, 2 * r.magnetic_coil
)
crystal_silicon = Recipe(F.smelter, 2, r.high_purity_silicon, r.crystal_silicon)
titanium_alloy = Recipe(
    F.smelter,
    12,
    4 * r.titanium_ingot + 4 * r.steel + 8 * r.sulfuric_acid,
    4 * r.titanium_alloy,
)
glass = Recipe(F.smelter, 2, 2 * r.stone, r.glass)
diamond = Recipe(F.smelter, 2, r.energetic_graphite, r.diamond)
x_ray_cracking = Recipe(
    F.oil_refinery,
    4,
    2 * r.hydrogen + r.refined_oil,
    3 * r.hydrogen + r.energetic_graphite,
)
organic_crystal = Recipe(
    F.chemical, 6, 2 * r.plastic + r.refined_oil + r.water, r.organic_crystal
)
graphene_from_fire_ice = Recipe(
    F.chemical, 2, 2 * r.fire_ice, 2 * r.graphene + r.hydrogen
)
hydrogen_fuel_rod = Recipe(
    F.assembler, 6, r.titanium_ingot + 10 * r.hydrogen, 2 * r.hydrogen_fuel_rod
)
deuteron_fuel_rod = Recipe(
    F.assembler,
    12,
    r.titanium_alloy + 20 * r.deuterium + r.super_magnetic_ring,
    2 * r.deuteron_fuel_rod,
)

# III
steel = Recipe(F.smelter, 3, 3 * r.iron_ingot, r.steel)
electric_motor = Recipe(
    F.assembler, 2, 2 * r.iron_ingot + r.gear + r.magnetic_coil, r.electric_motor
)
crystal_silicon_from_fractal = Recipe(
    F.assembler, 1.5, r.fractal_silicon, 2 * r.crystal_silicon
)
titanium_glass = Recipe(
    F.assembler,
    5,
    2 * r.glass + 2 * r.titanium_ingot + 2 * r.water,
    2 * r.titanium_glass,
)
prism = Recipe(F.assembler, 2, 3 * r.glass, 2 * r.prism)
diamond_from_kimberlite = Recipe(F.smelter, 1.5, r.kimberlite_ore, r.diamond)
deuterium_fractionation = Recipe(
    F.fractionator, 100 / 1800, 100 * r.hydrogen, r.deuterium + 99 * r.hydrogen
)
# organic crystal from organic materials not considered
titanium_crystal = Recipe(
    F.assembler, 4, r.organic_crystal + 3 * r.titanium_ingot, r.titanium_crystal
)
thruster = Recipe(F.assembler, 4, 2 * r.steel + 3 * r.copper_ingot, r.thruster)
reinforced_thruster = Recipe(
    F.assembler,
    6,
    5 * r.titanium_alloy + 5 * r.electromagnetic_turbine,
    r.reinforced_thruster,
)
strange_matter = Recipe(
    F.particle_collider,
    8,
    2 * r.particle_container + 2 * r.iron_ingot + 10 * r.deuterium,
    r.strange_matter,
)

# IV
gear = Recipe(F.assembler, 1, r.iron_ingot, r.gear)
electromagnetic_turbine = Recipe(
    F.assembler,
    2,
    2 * r.electric_motor + 2 * r.magnetic_coil,
    r.electromagnetic_turbine,
)
silicon_ore_from_stone = Recipe(F.smelter, 10, 10 * r.stone, r.silicon_ore)
circuit_board = Recipe(
    F.assembler, 1, 2 * r.iron_ingot + r.copper_ingot, 2 * r.circuit_board
)
graviton_lens = Recipe(
    F.assembler, 6, 4 * r.diamond + r.strange_matter, r.graviton_lens
)
sulfuric_acid = Recipe(
    F.chemical, 6, 6 * r.refined_oil + 8 * r.stone + 4 * r.water, 4 * r.sulfuric_acid
)
deuterium = Recipe(F.particle_collider, 5, 10 * r.hydrogen, 5 * r.deuterium)
plane_filter = Recipe(
    F.assembler, 12, r.casimir_crystal + 2 * r.titanium_glass, r.plane_filter
)
carbon_nanotube = Recipe(
    F.assembler, 4, 3 * r.graphene + r.titanium_ingot, 2 * r.carbon_nanotube
)
logistics_drone = Recipe(
    F.assembler,
    4,
    5 * r.iron_ingot + 2 * r.processor + 2 * r.thruster,
    r.logistics_drone,
)
logistics_vessel = Recipe(
    F.assembler,
    6,
    10 * r.titanium_alloy + 10 * r.processor + 2 * r.reinforced_thruster,
    r.logistics_vessel,
)

# V
plasma_exciter = Recipe(
    F.assembler, 2, 4 * r.magnetic_coil + 2 * r.prism, r.plasma_exciter
)
super_magnetic_ring = Recipe(
    F.assembler,
    3,
    2 * r.electromagnetic_turbine + 3 * r.magnet + r.energetic_graphite,
    r.super_magnetic_ring,
)
particle_broadband = Recipe(
    F.assembler,
    8,
    2 * r.carbon_nanotube + 2 * r.crystal_silicon + r.plastic,
    r.particle_broadband,
)
processor = Recipe(
    F.assembler,
    3,
    2 * r.circuit_board + 2 * r.microcrystalline_component,
    r.processor,
)
casimir_crystal = Recipe(
    F.assembler,
    4,
    r.titanium_crystal + 2 * r.graphene + 12 * r.hydrogen,
    r.casimir_crystal,
)
particle_container = Recipe(
    F.assembler,
    4,
    2 * r.electromagnetic_turbine + 2 * r.copper_ingot + 2 * r.graphene,
    r.particle_container,
)
space_warper = Recipe(F.assembler, 10, r.graviton_lens, r.space_warper)
carbon_nanotube_from_spiniform = Recipe(
    F.chemical, 4, 2 * r.spiniform_stalagmite_crystal, 2 * r.carbon_nanotube
)
solar_sail = Recipe(F.assembler, 4, r.graphene + r.photon_combiner, 2 * r.solar_sail)
frame_material = Recipe(
    F.assembler,
    6,
    4 * r.carbon_nanotube + r.titanium_alloy + r.high_purity_silicon,
    r.frame_material,
)
dyson_sphere_component = Recipe(
    F.assembler,
    8,
    3 * r.frame_material + 3 * r.solar_sail + 3 * r.processor,
    r.dyson_sphere_component,
)

# VI
photon_combiner = Recipe(
    F.assembler, 3, 2 * r.prism + r.circuit_board, r.photon_combiner
)
photon_combiner_from_optical = Recipe(
    F.assembler, 3, r.optical_grating_crystal + r.circuit_board, r.photon_combiner
)
microcrystalline_component = Recipe(
    F.assembler,
    2,
    2 * r.high_purity_silicon + r.copper_ingot,
    r.microcrystalline_component,
)
quantum_chip = Recipe(
    F.assembler, 6, 2 * r.processor + 2 * r.plane_filter, r.quantum_chip
)
casimir_crystal_from_optical = Recipe(
    F.assembler,
    4,
    4 * r.optical_grating_crystal + 2 * r.graphene + 12 * r.hydrogen,
    r.casimir_crystal,
)
particle_container_from_unipolar = Recipe(
    F.assembler, 4, 10 * r.unipolar_magnet + 2 * r.copper_ingot, r.particle_container
)
space_warper_from_gravity = Recipe(
    F.assembler, 10, r.gravity_matrix, 8 * r.space_warper
)

# VII
electromagnetic_matrix = Recipe(
    F.research_facility, 3, r.magnetic_coil + r.circuit_board, r.electromagnetic_matrix
)
energy_matrix = Recipe(
    F.research_facility, 6, 2 * r.energetic_graphite + 2 * r.hydrogen, r.enery_matrix
)
structure_matrix = Recipe(
    F.research_facility, 8, r.diamond + r.titanium_crystal, r.structure_matrix
)
information_matrix = Recipe(
    F.research_facility,
    10,
    2 * r.processor + r.particle_broadband,
    r.information_matrix,
)
gravity_matrix = Recipe(
    F.research_facility, 24, r.graviton_lens + r.quantum_chip, 2 * r.gravity_matrix
)
foundation = Recipe(F.assembler, 1, 3 * r.stone_brick + r.steel, r.foundation)
