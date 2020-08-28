# spectrum colors arranged by chance ii is a 38x38 grid

import numpy as np
from PIL import Image, ImageDraw, ImageFont


if __name__ == "__main__":

    im = Image.open("chance-ii.jpg")
    w, h = im.size

    delta_x = w / 38
    delta_y = h / 38
    
    draw = ImageDraw.Draw(im)
    offset = 15

    for x in range(38):
        for y in range(38):
            x_coord = offset + int(x * delta_x)
            y_coord = offset + int(y * delta_y)

            crop = im.crop((x_coord, y_coord, x_coord + 20, y_coord + 20))
            colors = list(
                np.average(np.average(np.array(crop), axis=0), axis=0)
            )
            r, g, b = [hex(int(color))[2:] for color in colors]

            draw.polygon(
                xy = [
                    (x_coord, y_coord),
                    (x_coord + 20, y_coord),
                    (x_coord + 20, y_coord + 20),
                    (x_coord, y_coord + 20),
                ],
                outline="white",
                fill=f"#{r + g + b}",
            )

    im.show()
