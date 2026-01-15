def draw_border_rectangle(w, h):
    top_border = "*" * w
    middle = "*" + " " * (w - 2) + "*"
    rect = top_border + "\n" + (middle + "\n") * (h - 2) + top_border

    return rect

if __name__ == '__main__':

    width = 20
    height = 10

    rectangle = draw_border_rectangle(width, height)

    print(rectangle)


