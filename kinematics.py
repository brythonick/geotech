#!/usr/bin/python
"""
=============================================================================
KINEMATIC ANALYSIS OF DISCONTINUITIES
=============================================================================
Filter a list of discontinuities to find any liable to slip with a given set
of slope parameters.
"""

from argparse import ArgumentParser
from functools import partial


# ============================================================================ #
# SCRIPT ARGUMENTS
# ============================================================================ #
parser = ArgumentParser()
required = parser.add_argument_group('required arguments')
required.add_argument("-i", "--input", help="TXT file with input values",
                      type=str, required=True)
required.add_argument("-a", "--angle", help="direction of rock face dip",
                      type=float, required=True)
required.add_argument("-d", "--dip", help="dip of rock face",
                      type=float, required=True)
required.add_argument("-f", "--friction", help="friction angle of the material",
                      type=float, required=True)
args = parser.parse_args()

with open(args.input) as open_file:
    discont_values = [val for val in open_file]
friction_angle = args.friction
face_direction = args.angle
face_dip = args.dip


# ============================================================================ #
# FUNCTIONS
# ============================================================================ #
def split_reading(reading):
    dip, dip_dir = reading.split("/")
    return float(dip), float(dip_dir)


# Functions to check sliding failure geometric rules:
def friction_rule(reading, friction):
    if reading[0] > friction:
        return True
    else:
        return False


def face_rule(reading, face):
    if reading[0] < face:
        return True
    else:
        return False


def direction_rule(reading, face_dir):
    if abs(face_dir - reading[1]) <= 20:
        return True
    else:
        return False


def sliding_failure(readings, face_dip, face_dir, friction):
    split_readings = map(split_reading, readings)
    failing_discont = filter(
        partial(friction_rule, friction=friction),
        split_readings
    )
    failing_discont = filter(
        partial(face_rule, face=face_dip),
        failing_discont
    )
    failing_discont = filter(
        partial(direction_rule, face_dir=face_dir),
        failing_discont
    )
    return failing_discont


def print_reading(reading):
    print("{0}/{1}".format(int(reading[0]), int(reading[1])))


# ============================================================================ #
# MAIN SCRIPT BLOCK
# ============================================================================ #
if __name__ == "__main__":
    failures = sliding_failure(discont_values, face_dip, face_direction,
                               friction_angle)
    map(print_reading, failures)
