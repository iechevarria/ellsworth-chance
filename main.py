# spectrum colors arranged by chance ii is a 38x38 grid

import numpy as np
from PIL import Image, ImageDraw, ImageFont

COLS = 38
ROWS = 38
OFFSET = 15

def int_to_hex(val):
    return hex(val)[:2]


def ints_to_hex_string(vals):
    """Given iterable w/ 3 elements, make hex string"""
    r, g, b = vals
    return f"#{int_to_hex(r) + int_to_hex(g) + int_to_hex(b)}"


if __name__ == "__main__":

    im = Image.open("chance-ii.jpg")
    w, h = im.size

    delta_x = w / COLS
    delta_y = h / ROWS

    tl_offset = OFFSET
    br_offset = int(delta_x - (2 * OFFSET))


    draw = ImageDraw.Draw(im)

    for x in range(COLS):
        for y in range(ROWS):
            x_coord = tl_offset + int(x * delta_x)
            y_coord = tl_offset + int(y * delta_y)

            crop = im.crop((
                x_coord,
                y_coord,
                x_coord + br_offset,
                y_coord + br_offset
            ))
            colors = list(
                np.average(np.average(np.array(crop), axis=0), axis=0)            
            )

            r, g, b = [hex(int(color))[2:] for color in colors]

            draw.polygon(
                xy = [
                    (x_coord, y_coord),
                    (x_coord + br_offset, y_coord),
                    (x_coord + br_offset, y_coord + br_offset),
                    (x_coord, y_coord + br_offset),
                ],
                outline="white",
                fill=f"#{r + g + b}",
            )

    im.show()
