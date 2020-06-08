#!/usr/bin/python3

from util import histogram
from sim import sim_data
from calc import interval_estimate
from definitions import *


def make_graph(iterations=100):
    for attempt in range(10):
        data = sim_data.SimData.load(path_saved_sim_data_hist)
        data.calc(iterations, attempt * iterations)

        inside_probability = 0.80
        interval = interval_estimate.estimate_interval(data.values, inside_probability)[0]

        width = 0.3
        for with_interval in [True, False]:
            if with_interval:
                arg_interval = interval
                postfix = "interval"
            else:
                arg_interval = None
                postfix = "no_interval"

            hist = histogram.Histogram(data.values, min_value=data.avg - width * data.avg,
                                       max_value=data.avg + width * data.avg, ints=True,
                                       interval=arg_interval)
            hist.draw_normal_distribution(data.mean, data.sigma, iterations)
            hist.show()
            hist.save("output/histogram_{}_{}_{}.png".format(iterations, postfix, attempt))


if __name__ == "__main__":
    make_graph(50)
    make_graph(1000)
