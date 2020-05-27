#!/usr/bin/python3

import numpy as np
from sim import simulation
import math
import json
from definitions import *


class SimData:

    def __init__(self, needle_count, sim_params=None):
        if sim_params is None:
            sim_params = [1, 2, 10, 50]
        self.sim_params = sim_params

        self.needle_count = needle_count

        self.sim = simulation.Simulation(*sim_params)

        self.avg = None
        self.p = None
        self.mean = None
        self.sigma = None
        self.values = []

    def generate(self, iterations):
        self.values = []
        for _ in range(iterations):
            result = self.sim.simulate(self.needle_count)
            self.values.append(result.needles_on_line)

    def calc(self, iterations=None):
        if iterations is not None:
            self.values = self.values[:iterations]
        self.avg = sum(self.values) / len(self.values)
        self.p = self.sim.probability()
        self.mean = self.needle_count * self.p
        self.variance = self.needle_count * self.p * (1 - self.p)
        self.sigma = math.sqrt(self.variance)

    def save(self, path=path_saved_sim_data):
        data = {
            "needle_count": self.needle_count,
            "sim_params": self.sim_params,
            "values": self.values
        }
        with open(path, 'w') as out_file:
            json.dump(data, out_file)

    @classmethod
    def load(cls, path=path_saved_sim_data):
        with open(path) as in_file:
            data = json.load(in_file)

        loaded_sim_data = cls(data["needle_count"], data["sim_params"])
        loaded_sim_data.values = data["values"]
        loaded_sim_data.calc()
        return loaded_sim_data


if __name__ == "__main__":
    sd = SimData(100)
    sd.generate(50)
    sd.calc()
    print(sd.values)
