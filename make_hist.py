#!/usr/bin/python3

from util import histogram
import simulation
import math
from calc import interval_estimate


def make_graph(iterations=100):
    data = []

    sim = simulation.Simulation(1, 2, 10, 50)

    n = 250

    for _ in range(iterations):
        result = sim.simulate(n)
        data.append(result.needles_on_line)

    p = sim.probability()
    mean = n * p
    sigma = math.sqrt(n * p * (1 - p))

    avg = sum(data) / len(data)
    inside_probability = 0.80
    interval = interval_estimate.estimate_interval(data, inside_probability)[0]
    interval_correct = interval[0] <= mean <= interval[1]

    width = 0.3
    hist = histogram.Histogram(data, min_value=avg - width * avg, max_value=avg + width * avg, ints=True,
                               interval=interval)
    hist.draw_normal_distribution(mean, sigma, iterations)
    hist.show()
    hist.save("output/histogram_{}.png".format(iterations))

    return interval_correct


if __name__ == "__main__":
    make_graph(50)
    make_graph(100)
    make_graph(1000)
    make_graph(10000)
    # make_graph(100000)
