import result as res
import random
import math


class Simulation:
    def __init__(self, needle_length, line_distance, line_count, height):
        self.needle_length = needle_length
        self.line_distance = line_distance
        self.line_count = line_count
        self.height = height

    def simulate(self, n):
        n = n
        result = res.Result(n, self.needle_length, self.line_distance, self.line_count, self.height)
        for i in range(n):
            x = random.uniform(0, self.line_count * self.line_distance)
            y = random.uniform(0, self.height)
            angle = random.uniform(0, 2*math.pi)
            result.add_needle(x, y, angle)
        return result

    def probability(self):
        if self.needle_length > self.line_distance:
            raise ArithmeticError()

        return (2*self.needle_length)/(self.line_distance*math.pi)
