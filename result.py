import math


class Result:
    def __init__(self, n, needle_length, line_distance, line_count, height):
        self.n = n
        self.needle_length = needle_length
        self.line_count = line_count
        self.height = height
        self.needles = []
        self.total_needles = 0
        self.needles_on_line = 0
        self.line_distance = line_distance

    def add_needle(self, x, y, angle):
        self.needles += [[x, y, angle, False]]
        self.total_needles += 1

        distance_to_line = (x + self.line_distance / 2) % self.line_distance
        distance_to_line = min(distance_to_line, self.line_distance - distance_to_line)
        needle_x_extent = abs(math.cos(angle)) * (self.needle_length / 2)
        if needle_x_extent >= distance_to_line:
            self.needles_on_line += 1
            self.needles[-1][3] = True
