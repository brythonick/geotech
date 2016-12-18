#!/usr/bin/python
"""
=============================================================================
ROCK MASS SLIDING
=============================================================================
Calculate the factor of safety for a rock mass above a sliding surface.
"""

from argparse import ArgumentParser
from math import sin, cos, tan, radians

# ============================================================================ #
# SCRIPT ARGUMENTS
# ============================================================================ #
parser = ArgumentParser()
parser.add_argument("-g", "--gravity", help="set the value of gravity",
                    type=float)
exclusive = parser.add_mutually_exclusive_group()
exclusive.add_argument("-b", "--bolt", type=float,
                       help="include a rock bolt, normal to slope")
exclusive.add_argument("-F", "--fos", type=float,
                       help="specify a FOS value to calculate a bolt for")
required = parser.add_argument_group('required arguments')
required.add_argument("-a", "--angle", help="sliding surface angle",
                      type=float, required=True)
required.add_argument("-f", "--friction", help="rock angle of friction",
                      type=float, required=True)
required.add_argument("-A", "--area", help="contact area of the rock mass",
                      type=float, required=True)
required.add_argument("-m", "--mass", help="mass of the rock block",
                      type=float, required=True)
args = parser.parse_args()

if not args.bolt:
    rock_bolt = 0
else:
    rock_bolt = args.bolt
if not args.gravity:
    gravity = 9.81
else:
    gravity = args.gravity
rock_mass = args.mass
slope_angle = args.angle
friction_angle = args.friction
contact_area = args.area
required_fos = args.fos


# ============================================================================ #
# FUNCTIONS
# ============================================================================ #
# TODO: add doc strings for functions
def force(mass, grav):
    return (mass * grav)/1000   # Force in kN


def normal(total_force, slope, bolt_force):
    return total_force * cos(radians(slope)) + bolt_force


def shear(total_force, slope):
    return total_force * sin(radians(slope))


def normal_stress(normal_force, area):
    return normal_force / area  # kN/m^2


def shear_stress(shear_force, area):
    return shear_force / area   # kN/m^2


def capacity(norm_stress, friction):
    return norm_stress * tan(radians(friction))


def fos(mass_capacity, mass_demand):
    return mass_capacity / mass_demand


# Functions for determining bolt tension required for FOS:
def capacity_required(fos_req, mass_demand):
    return fos_req * mass_demand


def normal_stress_required(cap_req, friction):
    return cap_req / tan(radians(friction))


def normal_required(normal_stress_req, area):
    return normal_stress_req * area


def tension_required(normal_req, block_force, slope):
    return normal_req - (block_force * cos(radians(slope)))


# ============================================================================ #
# MAIN SCRIPT BLOCK
# ============================================================================ #
if __name__ == "__main__":
    if not required_fos:
        fos_value = fos(
            capacity(
                normal_stress(
                    normal(force(rock_mass, gravity), slope_angle, rock_bolt),
                    contact_area
                ),
                friction_angle
            ),
            shear_stress(
                shear(force(rock_mass, gravity), slope_angle),
                contact_area
            )
        )
        print("{:0.3f}".format(fos_value))
    else:
        demand = shear_stress(
            shear(force(rock_mass, gravity), slope_angle),
            contact_area
        )
        tension_value = tension_required(
            normal_required(
                normal_stress_required(
                    capacity_required(required_fos, demand),
                    friction_angle
                ),
                contact_area
            ),
            force(rock_mass, gravity),
            slope_angle
        )
        print("{:0.2f}kN".format(tension_value))
    # TODO: add option for more verbose output, with individual calc results
