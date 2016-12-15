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
args = parser.parse_args()

gravity = args.gravity
slope_angle = args.angle
friction_angle = args.friction
area = args.area

# ============================================================================ #
# FUNCTIONS
# ============================================================================ #
# TODO func: calculate normal component
# TODO func: calculate shear component
# TODO func: calculate normal stress
# TODO func: calculate shear stress
# TODO func: calculate demand
# TODO func: calculate capacity
# TODO func: calculate FOS

# ============================================================================ #
# MAIN SCRIPT BLOCK
# ============================================================================ #
if __name__ == "__main__":
    # TODO call: calculate FOS
    pass
