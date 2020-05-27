#!/usr/bin/python3

from util import histogram
from sim import sim_data
from calc import interval_estimate


def make_graph(iterations=100):
    data = sim_data.SimData.load()
    data.calc(iterations)

    inside_probability = 0.80
    interval = interval_estimate.estimate_interval(data.values, inside_probability)[0]
    interval_correct = interval[0] <= data.mean <= interval[1]

    width = 0.3
    hist = histogram.Histogram(data.values, min_value=data.avg - width * data.avg,
                               max_value=data.avg + width * data.avg, ints=True,
                               interval=interval)
    hist.draw_normal_distribution(data.mean, data.sigma, iterations)
    hist.show()
    hist.save("output/histogram_{}.png".format(iterations))

    return interval_correct


if __name__ == "__main__":
    make_graph(50)
    make_graph(100)
    make_graph(1000)
    make_graph(10000)
    make_graph(100000)
