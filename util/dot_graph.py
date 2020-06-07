#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math
from definitions import *


class DotGraph:
    def __init__(self, x, y1, y2=None):
        self.fig, self.ax = plt.subplots(1, 1, tight_layout=True, figsize=(plot_width, plot_height), dpi=plot_dpi)

        self.ax.plot(x, y1, color=color_dot_1, linestyle="", marker="D")
        if y2 is not None:
            self.ax.plot(x, y2, color=color_dot_2, linestyle="", marker="o")
        self.ax.plot([0, 1], [1, 1], color=color_flat_line, linestyle=":", marker="")
        self.ax.set_ylim(0.9, 1.1)

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
