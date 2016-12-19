#!/usr/bin/python
"""
=============================================================================
CHARACTERISTIC VALUE
=============================================================================
Determine a characteristic value from a set of observed values. As in Eurocode
7.
"""

from argparse import ArgumentParser
from scipy import stats
from math import sqrt
from numpy import std


# ============================================================================ #
# SCRIPT ARGUMENTS
# ============================================================================ #
parser = ArgumentParser()
parser.add_argument("-i", "--input", help="TXT file with input values",
                    type=str)
args = parser.parse_args()

with open(args.input) as open_file:
    obs_values = [float(val) for val in open_file]


# ============================================================================ #
# FUNCTIONS
# ============================================================================ #
def mean(values):
    return sum(values) / len(values)


def stat_coefficient_5(num_samples):
    # Variance unknown, 95% confidence, 5% fractile
    n = num_samples - 1
    return stats.t.ppf(0.95, n) * sqrt(1.0 + 1/num_samples)


def stat_coefficient_50(num_samples):
    # Variance unknown, 95% confidence, 50% fractile
    n = num_samples - 1
    return stats.t.ppf(0.95, n) * sqrt(1.0/num_samples)


def characteristic_value(values):
    char_val_5 = mean(values) - \
                 (stat_coefficient_5(len(values)) * std(values))
    char_val_50 = mean(values) - \
                  (stat_coefficient_50(len(values)) * std(values))
    return char_val_50, char_val_5


# ============================================================================ #
# MAIN SCRIPT BLOCK
# ============================================================================ #
if __name__ == "__main__":
    char_vals = characteristic_value(obs_values)
    print("Characteristic Mean: {:d}".format(int(round(char_vals[0]))))
    print("Characteristic Low:  {:d}".format(int(round(char_vals[1]))))
