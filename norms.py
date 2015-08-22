import sys


MODE = "text" if "text" in sys.argv else "spacing"

print """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style type="text/css">
            body {
                font-size: 1.5em;
                padding: 1.5em;"""

if MODE == "text":
    print 'font-family: "Gill Sans", "Gill Sans MT", sans-serif;'
else:
    print 'font-faily: "Times New Roman", Times, Georgia, serif;'
print """
            }

            h1 {
                font-family: "Gill Sans", "Gill Sans MT", sans-serif;
                font-weight: 700;
                font-size: .9em;
                margin-bottom: 3em;
            }

            td {
                padding-right: .5em;
                padding-bottom: 10px;
                width: 1px;
                white-space: nowrap;
            }

        </style>
    </head>

    <body>

        <h1>Quadrats (CSS points)</h1>

        <table>

"""


x_point_sizes = (5, 6, 7, 8, 9, 10, 12, 14, 18, 24, 30, 36, 42)
y_point_sizes = (
    5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 36,
    40, 42, 48, 54, 56, 60, 72, 84, 90, 96, 108, 120, 126, 144, 168
)
offset = x_point_sizes[0]

rows = []

for ptsize in x_point_sizes:
    row = []
    for cell in [i for i in range(offset, 169) if i in y_point_sizes]:
        if len([i for i in row if i is not None]) == 4:
            row.append(None)
            continue
        if (ptsize == cell or (cell % ptsize == 0)):
            row.append(cell)
        else:
            row.append(None)
    assert len([x for x in row if x is not None]) == 4
    rows.append(row)

for row_idx, row in enumerate(rows):
    print "<tr>"
    found = 0
    for td_idx, td in enumerate(row):
        if MODE == "text":
            print "<td>"
            print td if td else " "
            print "</td>"
        else:
            print '<td style="font-size: ' + str(x_point_sizes[row_idx]) + 'pt;">'
            if td:
                found += 1
                cell_pt_size = y_point_sizes[td_idx]
                if False:  # TODO: the most important part
                    print "<span style='background-color: red;'>"
                else:
                    print "<span style='background-color: black;'>"
                for k in range(1, found + 1):
                    print "&#x2001;"
                print "</span>"
            else:
                print " "
            print "</td>"
    print "</tr>"

print "</table></body></html>"
