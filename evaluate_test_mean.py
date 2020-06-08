#!/usr/bin/python3

import numpy as np
from calc import test_mean
from util import dot_graph
from sim import sim_data

data = None


def iteration(values, mean, error_probability, make_intentional_error, debug=False):
    return test_mean.test_mean(values, mean, error_probability, make_intentional_error, debug)


def evaluate_test_mean(inside_probability, iterations=100):
    positive_count_right = 0
    positive_count_wrong = 0

    for i in range(iterations):
        values = data.values[i * 20:(i + 1) * 20]

        if iteration(values, data.mean, inside_probability, make_intentional_error=False):
            positive_count_right += 1
        if iteration(values, data.mean, inside_probability, make_intentional_error=True):
            positive_count_wrong += 1

    print()
    print("iterations", iterations, "  inside_probability", inside_probability)
    print("positive_count", positive_count_right, positive_count_wrong)
    print("positive_count/iterations", positive_count_right / iterations, positive_count_wrong / iterations)

    return 1 - positive_count_right / iterations, 1 - positive_count_wrong / iterations


def make_graph(iterations=100):
    x = np.linspace(0, 1, 10 + 1)[1:-1]
    y_right = []
    y_wrong = []
    # y_wrong = None
    for x_val in x:
        right, wrong = evaluate_test_mean(x_val, iterations)
        y_right.append(right / x_val)
        y_wrong.append(wrong / x_val)

    print(x)
    print(y_right)
    print(y_wrong)
    dg = dot_graph.DotGraph(x, y_right, y_wrong)
    dg.show()
    dg.save("output/mean_test.png")


if __name__ == "__main__":
    data = sim_data.SimData.load()
    print("len(data.values)", len(data.values))
    make_graph(10 ** 5)
