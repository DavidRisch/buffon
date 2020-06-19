from PIL import Image, ImageDraw
import math


def create_image(path, result):
    scale = 100
    img = Image.new('RGB', (result.needle_length * 2 * result.line_count * scale, result.height * scale), color='white')
    d = ImageDraw.Draw(img)
    line_color = (0, 0, 0)
    for x in range(result.line_count):
        d.line([((result.line_distance * x + result.line_distance / 2) * scale, 0),
                ((result.line_distance * x + result.line_distance / 2) * scale, result.height * scale)],
               fill=line_color, width=10)
    needle_color_default = (255, 0, 0)
    needle_color_hit = "#0090c6ff"
    for needle in result.needles:
        x = needle[0]
        y = needle[1]
        angle = needle[2]

        x1 = x + math.cos(angle) * result.needle_length / 2
        x2 = x - math.cos(angle) * result.needle_length / 2
        y1 = y + math.sin(angle) * result.needle_length / 2
        y2 = y - math.sin(angle) * result.needle_length / 2
        d.line([(x1 * scale, y1 * scale), (x2 * scale, y2 * scale)],
               fill=needle_color_hit if needle[3] else needle_color_default, width=10)
    img.save(path)
