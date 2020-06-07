#!/usr/bin/python3

import numpy as np
from calc import interval_estimate
from util import dot_graph
from sim import sim_data

mean = 5
sigma = 1


def dummy_data():  # TODO: use sim_data
    x = np.random.randn(20)
    x *= sigma
    x += mean

    return x


def iteration(values, sigma, inside_probability, make_intentional_error, debug=False):
    interval = interval_estimate.estimate_interval(values, inside_probability, make_intentional_error, debug=debug)[1]
    return interval[0] <= sigma <= interval[1]


def evaluate_interval(inside_probability, iterations=100):
    positive_count_right = 0
    positive_count_wrong = 0

    for i in range(iterations):
        values = dummy_data()

        if iteration(values, sigma, inside_probability, make_intentional_error=False):
            positive_count_right += 1
        if iteration(values, sigma, inside_probability, make_intentional_error=True):
            positive_count_wrong += 1

    print()
    print("iterations", iterations, "  inside_probability", inside_probability)
    print("positive_count", positive_count_right, positive_count_wrong)
    print("positive_count/iterations", positive_count_right / iterations, positive_count_wrong / iterations)

    return positive_count_right / iterations, positive_count_wrong / iterations


def make_graph(iterations=100):
    x = np.linspace(0, 1, 10 + 1)[1:-1]
    y_right = []
    y_wrong = []
    # y_wrong = None
    for x_val in x:
        right, wrong = evaluate_interval(x_val, iterations)
        y_right.append(right / x_val)
        y_wrong.append(wrong / x_val)

    print(x)
    print(y_right)
    print(y_wrong)

    dg = dot_graph.DotGraph(x, y_right, y_wrong)
    dg.show()
    dg.save("output/var_interval.png")


if __name__ == "__main__":
    make_graph(10 ** 5)
