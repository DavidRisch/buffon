#!/usr/bin/python3

import numpy as np
import test_mean


def dummy_data():
    x = np.random.randn(100)
    x *= 0.2
    x += 5

    return x


def iteration(debug=False):
    return test_mean.test_mean(dummy_data(), 5, 0.15, debug)


def evaluate_test_mean(iterations=100):
    positive_count = 0

    for _ in range(iterations):
        if iteration():
            positive_count += 1

    print()
    print("iterations", iterations)
    print("positive_count", positive_count)
    print("positive_count/iterations", positive_count / iterations)


if __name__ == "__main__":
    evaluate_test_mean(50000)
