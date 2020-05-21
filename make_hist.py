#!/usr/bin/python3

from util import histogram
import simulation
import math


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

    print(data[:100])

    avg = sum(data) / len(data)

    width = 0.3

    hist = histogram.Histogram(data, min_value=avg - width * avg, max_value=avg + width * avg, ints=True)
    hist.draw_normal_distribution(mean, sigma, iterations)
    hist.show()
    hist.save("output/histogram_{}.png".format(iterations))


if __name__ == "__main__":
    make_graph(1000)
    make_graph(10000)
    make_graph(100000)
