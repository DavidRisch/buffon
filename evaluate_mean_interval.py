#!/usr/bin/python3

import numpy as np
from calc import interval_estimate
from util import dot_graph
from sim import sim_data


def iteration(values, mean, inside_probability, debug=False):
    interval = interval_estimate.estimate_interval(values, inside_probability, debug=debug)[0]
    return interval[0] <= mean <= interval[1]


def evaluate_interval(inside_probability, iterations=100):
    positive_count = 0

    data = sim_data.SimData.load()
    batch_size = 100
    for i in range(iterations):
        values = data.values[i * batch_size:i * batch_size + batch_size]

        if iteration(values, data.mean, inside_probability):
            positive_count += 1

    print()
    print("iterations", iterations, "  inside_probability", inside_probability)
    print("positive_count", positive_count)
    print("positive_count/iterations", positive_count / iterations)

    return positive_count / iterations


def make_graph(iterations=100):
    x = np.linspace(0, 0.99, 20 + 1)
    y = []
    for x_val in x:
        y.append(evaluate_interval(x_val, iterations))

    print(x)
    print(y)

    dg = dot_graph.DotGraph(x, y)
    dg.show()
    dg.save("output/mean_interval.png")


if __name__ == "__main__":
    make_graph(1000)
    # evaluate_test_mean(50000)
