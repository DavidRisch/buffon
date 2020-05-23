#!/usr/bin/python3

import numpy as np
from sim import simulation
import math


def dummy_data():
    x = np.random.randn(100)
    x *= 0.2
    x += 5

    return x


class SimData:

    def __init__(self, iterations, needle_count):
        self.values = []

        sim = simulation.Simulation(1, 2, 10, 50)

        for _ in range(iterations):
            result = sim.simulate(needle_count)
            self.values.append(result.needles_on_line)

        self.p = sim.probability()
        self.mean = needle_count * self.p
        self.sigma = math.sqrt(needle_count * self.p * (1 - self.p))
        self.avg = sum(self.values) / len(self.values)


if __name__ == "__main__":
    data = SimData(100, 50)
    print(data.values)
