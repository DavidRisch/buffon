import math


class Result:
    def __init__(self, n, needle_length, line_count, height):
        self.n = n
        self.needle_length = needle_length
        self.line_count = line_count
        self.height = height
        self.needles = []
        self.total_needles = 0
        self.needles_on_line = 0

    def add_needle(self, x, y, angle):
        self.needles += [[x, y, angle]]
        self.total_needles += 1

        x_mod = x % self.needle_length * 2
        needle_x_width = abs(math.cos(angle)) * (self.needle_length / 2)
        if x_mod - needle_x_width < self.needle_length and x_mod + needle_x_width < self.needle_length:
            self.needles_on_line += 1
