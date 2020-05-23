#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math
from definitions import *


class DotGraph:
    def __init__(self, x, y):
        self.fig, self.ax = plt.subplots(1, 1, tight_layout=True, figsize=(plot_width, plot_height), dpi=plot_dpi)

        self.ax.plot(x, y, color=color_dot, linestyle="", marker="o")

    def save(self, path):
        self.fig.savefig(path)

    def show(self):
        self.fig.show()


if __name__ == "__main__":
    np.random.seed(19680801)
    N_points = 50

    y = np.random.randn(N_points)
    y *= 0.2
    y += math.pi

    dg = DotGraph(range(len(y)), y)
    dg.show()
