from mako.template import Template


# all known point sizes; the ones that determine the x-axis
all_point_sizes = (
    5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32,
    36, 40, 42, 48, 54, 56, 60, 72, 84, 90, 96, 108, 120, 126, 144, 168
)

# the commonly-used (there is a better term) sizes; the ones used on the y-axis
common_point_sizes = (5, 6, 7, 8, 9, 10, 12, 14, 18, 24, 30, 36, 42, 48, 60, 72)

# the max point size on the y-axis
y_axis_max = 42

# a 4-em quad is the largest piece of spacing material we would have
max_quad_size = 4


def main():
    matrix = []
    rows = enumerate([x for x in common_point_sizes if x <= y_axis_max])

    for row_idx, y_size in rows:
        row = []

        for x_size in all_point_sizes:
            display_quad = x_size == y_size or (x_size % y_size == 0)
            quads_displayed = len([x for x in row if x])
            if display_quad and quads_displayed < max_quad_size:
                cell = {
                    'multiple': x_size != y_size and x_size in common_point_sizes,
                    'width': str(x_size),
                    'height':  str(common_point_sizes[row_idx])
                }
            else:
                cell = None
            row.append(cell)

        matrix.append(row)

    print(Template(filename="template.html").render(rows=matrix))


if __name__ == "__main__":
    main()
