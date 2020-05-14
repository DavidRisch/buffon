#!/usr/bin/python3

import math
from scipy.stats import t as t_student


def test_mean(data, target_mean, error_probability, debug=False):
    n = len(data)
    degrees_of_freedom = n - 1
    observed_mean = sum(data) / n
    estimated_std_deviation = math.sqrt(1 / (n - 1) * sum([(point - observed_mean) ** 2 for point in data]))

    c = t_student.ppf(1 - error_probability / 2, degrees_of_freedom)

    t_hat = (observed_mean - target_mean) / (estimated_std_deviation / math.sqrt(n))

    if debug:
        print()
        print("target_mean", target_mean, "  error_probability", error_probability)
        print("observed_mean", observed_mean)
        print("estimated_std_deviation", estimated_std_deviation)
        print("c", c)
        print("t_hat", t_hat)

    c = abs(c)
    return -c <= t_hat <= c


if __name__ == "__main__":
    print(test_mean([1.99, 2, 2.01], 2, 0.05, True))
    print(test_mean([1, 2, 3.3], 2, 0.20, True))
    print(test_mean([1, 2, 3.3], 2, 0.90, True))
    print(test_mean([11, 12, 13], 2, 0.05, True))
