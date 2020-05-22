#!/usr/bin/python3

import numpy as np
import interval_estimate
import dot_graph


def dummy_data():
    x = np.random.randn(100)
    x *= 0.2
    x += 5

    return x


def iteration(inside_probability, debug=False):
    interval = interval_estimate.estimate_interval(dummy_data(), inside_probability, debug=debug)
    return interval[0] <= 5 <= interval[1]


def evaluate_interval(inside_probability, iterations=100):
    positive_count = 0

    for _ in range(iterations):
        if iteration(inside_probability):
            positive_count += 1

    print()
    print("iterations", iterations, "  inside_probability", inside_probability)
    print("positive_count", positive_count)
    print("positive_count/iterations", positive_count / iterations)

    return positive_count / iterations


def make_graph(iterations=100):
    x = np.linspace(0, 1, 20 + 1)
    y = []
    for x_val in x:
        y.append(evaluate_interval(x_val, iterations))

    print(x)
    print(y)

    dg = dot_graph.DotGraph(x, y)
    dg.show()
    dg.save("output/interval_estimates.png")


if __name__ == "__main__":
    make_graph(1000)
    # evaluate_test_mean(50000)
