#!/usr/bin/python3

import numpy as np
from calc import test_mean
from util import dot_graph


def dummy_data():
    x = np.random.randn(100)
    x *= 0.2
    x += 5

    return x


def iteration(error_probability, debug=False):
    return test_mean.test_mean(dummy_data(), 5, error_probability, debug)


def evaluate_test_mean(error_probability, iterations=100):
    positive_count = 0

    for _ in range(iterations):
        if iteration(error_probability):
            positive_count += 1

    print()
    print("iterations", iterations, "  error_probability", error_probability)
    print("positive_count", positive_count)
    print("positive_count/iterations", positive_count / iterations)

    return positive_count / iterations


def make_graph(iterations=100):
    x = np.linspace(0, 1, 20 + 1)
    y = []
    for x_val in x:
        y.append(evaluate_test_mean(x_val, iterations))

    print(x)
    print(y)

    dg = dot_graph.DotGraph(x, y)
    dg.show()
    dg.save("output/parameter_tests.png")


if __name__ == "__main__":
    make_graph(1000)
    # evaluate_test_mean(50000)
