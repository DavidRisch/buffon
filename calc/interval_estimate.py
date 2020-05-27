#!/usr/bin/python3

import math
import numpy as np
from scipy.stats import t as t_student
from scipy.stats import chi2


def estimate_interval(data, inside_probability, debug=False):
    n = len(data)
    degrees_of_freedom = n - 1
    observed_mean = sum(data) / n
    estimated_std_deviation = math.sqrt(1 / (n - 1) * sum([(point - observed_mean) ** 2 for point in data]))

    # confidence interval: mean
    c = t_student.ppf((inside_probability + 1) / 2, degrees_of_freedom)  # ppf = "Percent point function"

    half_delta = (c * estimated_std_deviation) / math.sqrt(n)

    mean_l = observed_mean - half_delta
    mean_h = observed_mean + half_delta

    # confidence interval: variance
    error_probability = 1 - inside_probability
    c_1 = chi2.ppf(error_probability / 2, degrees_of_freedom)
    c_2 = chi2.ppf(1 - error_probability / 2, degrees_of_freedom)

    sigma_l = math.sqrt(degrees_of_freedom * (estimated_std_deviation ** 2) / c_2)
    sigma_h = math.sqrt(degrees_of_freedom * (estimated_std_deviation ** 2) / c_1)
    sigma_l, sigma_h = map(
        lambda c_n: math.sqrt(degrees_of_freedom * (estimated_std_deviation ** 2) / c_n),
        [c_2, c_1])  # order is intentionally inverted

    if debug:
        print()
        print("inside_probability", inside_probability)
        print("observed_mean", observed_mean)
        print("estimated_std_deviation", estimated_std_deviation)
        print("c", c, "  mean_l", mean_l, "  mean_h", mean_h)
        inside = sum([1 for x in data if mean_l <= x <= mean_h])
        print("inside", inside, "  inside/n", inside / n)
        print("c", c, "  sigma_l", sigma_l, "  sigma_h", sigma_h)

    return [mean_l, mean_h], [sigma_l, sigma_h]


if __name__ == "__main__":
    dummy_data = np.random.randn(1000)
    dummy_data *= 0.6
    dummy_data += 5
    print(estimate_interval(dummy_data, 0.99, True))
    print(estimate_interval(dummy_data, 0.95, True))
    print(estimate_interval(dummy_data, 0.90, True))
    print(estimate_interval(dummy_data, 0.50, True))
