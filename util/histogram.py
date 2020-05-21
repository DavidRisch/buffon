#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm


class Histogram:
    def __init__(self, data, min_value=2.6, max_value=3.7, bin_number=20, ints=False):
        self.min_value = min_value
        self.max_value = max_value
        if ints:
            self.min_value = math.floor(self.min_value) - 0.5
            self.max_value = math.ceil(self.max_value) + 0.5
            bin_number = round(self.max_value - self.min_value)

        self.fig, self.ax = plt.subplots(1, 1, tight_layout=True)

        bins = self.generate_bins(self.min_value, self.max_value, bin_number)

        self.ax.hist(data, bins=bins)
        self.ax.grid()

    def draw_normal_distribution(self, mean, sigma, iterations):
        x_axis = np.arange(self.min_value, self.max_value, 0.001)
        norm_data = iterations * norm.pdf(x_axis, mean, sigma)
        plt.plot(x_axis, norm_data, color="r")

    def save(self, path):
        self.fig.savefig(path)

    def show(self):
        self.fig.show()

    @staticmethod
    def generate_bins(min_value, max_value, count):
        width = (max_value - min_value) / count
        return [min_value + width * i for i in range(count + 1)]


if __name__ == "__main__":
    np.random.seed(19680801)
    N_points = 1000

    x = np.random.randn(N_points)
    x *= 0.2
    x += math.pi

    print(x)

    hist = Histogram(x)
    hist.show()