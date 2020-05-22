#!/usr/bin/python3

import math
import numpy as np
from scipy.stats import t as t_student


def estimate_interval(data, inside_probability, debug=False):
    n = len(data)
    degrees_of_freedom = n - 1
    observed_mean = sum(data) / n
    estimated_std_deviation = math.sqrt(1 / (n - 1) * sum([(point - observed_mean) ** 2 for point in data]))

    c = t_student.ppf((inside_probability + 1) / 2, degrees_of_freedom)  # ppf = "Percent point function"

    half_delta = (c * estimated_std_deviation) / math.sqrt(n)

    c_1 = observed_mean - half_delta
    c_2 = observed_mean + half_delta

    if debug:
        print()
        print("inside_probability", inside_probability)
        print("observed_mean", observed_mean)
        print("estimated_std_deviation", estimated_std_deviation)
        print("c", c, "  c_1", c_1, "  c_2", c_2)
        inside = sum([1 for x in data if c_1 <= x <= c_2])
        print("inside", inside, "  inside/n", inside / n)

    return [c_1, c_2]


if __name__ == "__main__":
    dummy_data = np.random.randn(1000)
    dummy_data *= 0.6
    dummy_data += 5
    print(estimate_interval(dummy_data, 0.99, True))
    print(estimate_interval(dummy_data, 0.95, True))
    print(estimate_interval(dummy_data, 0.90, True))
    print(estimate_interval(dummy_data, 0.50, True))
