import result as res
import random
import math


class Simulation:
    def __init__(self, needle_length, line_count, height):
        self.needle_length = needle_length
        self.line_count = line_count
        self.height = height

    def simulate(self, n):
        n = n
        result = res.Result(n, self.needle_length, self.line_count, self.height)
        for i in range(n):
            x = random.uniform(0, self.line_count * self.needle_length * 2)
            y = random.uniform(0, self.height)
            angle = random.uniform(0, 2*math.pi)
            result.add_needle(x, y, angle)
        return result
