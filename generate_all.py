#!/usr/bin/python3

import evaluate_test_mean
import evaluate_mean_interval
import make_hist
import needle_image

evaluate_test_mean.make_graph(1000)

evaluate_mean_interval.make_graph(1000)

make_hist.make_graph(50)
make_hist.make_graph(100)
make_hist.make_graph(1000)
make_hist.make_graph(10000)

needle_image.make_image()
