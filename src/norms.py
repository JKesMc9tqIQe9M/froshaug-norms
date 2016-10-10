from mako.template import Template


# TODO add back the text mode stuff


# all known point sizes, and the ones that determine the x-axis
x_axis_sizes = (
    5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32,
    36, 40, 42, 48, 54, 56, 60, 72, 84, 90, 96, 108, 120, 126, 144, 168
)

# normative sizes, and the ones we use for the y-axis
normal_point_sizes = (5, 6, 7, 8, 9, 10, 12, 14, 18, 24, 30, 36, 42, 48, 60, 72)

# point size for the final row
y_axis_max = 42

# a 4-em quad is the largest piece of spacing material we have here
max_quad_size = 4


def make_norms():

    # first pass to build the table of values
    matrix = []
    for ptsize in [x for x in normal_point_sizes if x <= y_axis_max]:
        row = []
        cols = [i for i in range(min(x_axis_sizes), max(x_axis_sizes) + 1) if i in x_axis_sizes]
        for c in cols:
            cell_value = None
            if len([i for i in row if i is not None]) < max_quad_size:
                if ptsize == c or (c % ptsize == 0):
                    cell_value = c
            row.append(cell_value)
        matrix.append(row)

    # second pass to assemble what we need for rendering in the template
    output_rows = []
    for row_idx, row in enumerate(matrix):
        cells = []
        for td_idx, td in enumerate(row):
            cell = {}
            if td:
                column_pt_size = x_axis_sizes[td_idx]
                multiple_use_size = (
                    column_pt_size != normal_point_sizes[row_idx] and
                    column_pt_size in normal_point_sizes
                )
                cell = {
                    'multiple': multiple_use_size,
                    'width': column_pt_size,
                    'height':  str(normal_point_sizes[row_idx])
                }
            cells.append(cell)
        output_rows.append(cells)

    print(Template(filename="template.html").render(rows=output_rows))

if __name__ == "__main__":
    make_norms()
