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
                    action="store_true")
parser.add_argument("-a", "--angle", help="sliding surface angle",
                    action="store_true")
parser.add_argument("-f", "--friction", help="rock angle of friction",
                    action="store_true")
parser.add_argument("-A", "--area", help="contact area of the rock mass",
                    action="store_true")
args = parser.parse_args()

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
