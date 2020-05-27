#!/usr/bin/python3

import numpy as np
from calc import test_mean
from util import dot_graph
from sim import sim_data


def iteration(values, mean, error_probability, debug=False):
    return test_mean.test_mean(values, mean, error_probability, debug)


def evaluate_test_mean(error_probability, iterations=100):
    positive_count = 0

    data = sim_data.SimData.load()
    batch_size = 100
    for i in range(iterations):
        values = data.values[i * batch_size:i * batch_size + batch_size]
        if iteration(values, data.mean, error_probability):
            positive_count += 1

    print()
    print("iterations", iterations, "  error_probability", error_probability)
    print("positive_count", positive_count)
    print("positive_count/iterations", positive_count / iterations)

    return 1 - positive_count / iterations


def make_graph(iterations=100):
    x = np.linspace(0, 0.9999, 20 + 1)
    y = []
    for x_val in x:
        y.append(evaluate_test_mean(x_val, iterations))

    print(x)
    print(y)

    dg = dot_graph.DotGraph(x, y)
    dg.show()
    dg.save("output/mean_test.png")


if __name__ == "__main__":
    make_graph(1000)
    # evaluate_test_mean(50000)
