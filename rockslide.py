#!/usr/bin/python3
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
parser.add_argument("-a", "--angle", help="sliding surface angle",
                    type=float)
parser.add_argument("-f", "--friction", help="rock angle of friction",
                    type=float)
parser.add_argument("-A", "--area", help="contact area of the rock mass",
                    type=float)
parser.add_argument("-m", "--mass", help="mass of the rock block",
                    type=float)
args = parser.parse_args()

rock_mass = args.mass
gravity = args.gravity
slope_angle = args.angle
friction_angle = args.friction
contact_area = args.area


# ============================================================================ #
# FUNCTIONS
# ============================================================================ #
def force(mass, grav):
    return (mass * grav)/1000   # Force in kN


def normal(total_force, slope):
    return total_force * cos(radians(slope))


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


# ============================================================================ #
# MAIN SCRIPT BLOCK
# ============================================================================ #
if __name__ == "__main__":
    fos_value = fos(
        capacity(
            normal_stress(
                normal(force(rock_mass, gravity), slope_angle),
                contact_area
            ),
            friction_angle
        ),
        shear_stress(
            shear(force(rock_mass, gravity), slope_angle),
            contact_area
        )
    )
    print("{:0.2f}".format(fos_value))
