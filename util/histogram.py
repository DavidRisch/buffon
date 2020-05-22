#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm
from definitions import *


class Histogram:
    def __init__(self, data, min_value=2.6, max_value=3.7, bin_number=20, interval=None, color_interval=False,
                 ints=False):
        self.min_value = min_value
        self.max_value = max_value
        if ints:
            self.min_value = math.floor(self.min_value) - 0.5
            self.max_value = math.ceil(self.max_value) + 0.5
            bin_number = round(self.max_value - self.min_value)

        self.fig, self.ax = plt.subplots(1, 1, tight_layout=True)

        bins, bin_width = self.generate_bins(self.min_value, self.max_value, bin_number)

        _, _, patches = self.ax.hist(data, bins=bins, color=color_histogram_normal)
        self.ax.grid()

        if interval is not None:
            for border in interval:
                self.ax.axvline(border, c=color_histogram_border)
            if color_interval:
                for patch in patches:
                    if interval[0] <= patch.get_x() + patch.get_width() / 2 <= interval[1]:
                        patch.set_facecolor(color_histogram_inside)
                    else:
                        patch.set_facecolor(color_histogram_normal)

    def draw_normal_distribution(self, mean, sigma, iterations):
        x_axis = np.arange(self.min_value, self.max_value, 0.001)
        norm_data = iterations * norm.pdf(x_axis, mean, sigma)
        plt.plot(x_axis, norm_data, color=color_histogram_ideal)

    def save(self, path):
        self.fig.savefig(path)

    def show(self):
        self.fig.show()

    @staticmethod
    def generate_bins(min_value, max_value, count):
        width = (max_value - min_value) / count
        return [min_value + width * i for i in range(count + 1)], width


if __name__ == "__main__":
    np.random.seed(19680801)
    N_points = 1000

    x = np.random.randn(N_points)
    x *= 0.2
    x += math.pi

    # print(x)

    hist = Histogram(x, interval=[2.8, 3])
    hist.show()
