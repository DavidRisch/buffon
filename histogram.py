import matplotlib.pyplot as plt
import numpy as np
import math


class Histogram:
    def __init__(self, data, min_value=2.6, max_value=3.7, bin_number=20):
        self.fig, self.ax = plt.subplots(1, 1, tight_layout=True)

        self.ax.hist(data, bins=self.generate_bins(min_value, max_value, bin_number))
        self.ax.axvline(math.pi, color="#000000FF")

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

    hist = Histogram(x)
    hist.show()
