import sys


MODE = "text" if "text" in sys.argv else "spacing"

print """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Typographic norms</title>
        <style type="text/css">

            @font-face {
                font-family: 'humanst521_btroman';
                src: url('fonts/humanist_521_bt-webfont.eot');
                src: url('fonts/humanist_521_bt-webfont.eot?#iefix') format('embedded-opentype'),
                     url('fonts/humanist_521_bt-webfont.woff2') format('woff2'),
                     url('fonts/humanist_521_bt-webfont.woff') format('woff'),
                     url('fonts/humanist_521_bt-webfont.ttf') format('truetype'),
                     url('fonts/humanist_521_bt-webfont.svg#humanst521_btroman') format('svg');
                font-weight: normal;
                font-style: normal;
            }

            @font-face {
                font-family: 'humanst521_btbold';
                src: url('fonts/humanist_521_bold_bt-webfont.eot');
                src: url('fonts/humanist_521_bold_bt-webfont.eot?#iefix') format('embedded-opentype'),
                     url('fonts/humanist_521_bold_bt-webfont.woff2') format('woff2'),
                     url('fonts/humanist_521_bold_bt-webfont.woff') format('woff'),
                     url('fonts/humanist_521_bold_bt-webfont.ttf') format('truetype'),
                     url('fonts/humanist_521_bold_bt-webfont.svg#humanst521_btbold') format('svg');
                font-weight: 700;
                font-style: normal;
            }

            body {
                font-size: 1.4em;
                padding: 1em .75em 1em .75em;
"""

if MODE == "text":
    print 'font-family: humanst521_btroman, sans-serif;'
else:
    print 'font-faily: "Times New Roman", Times, Georgia, serif;'
print """
            }

            h1 {
                font-family: humanst521_btbold, sans-serif;
                font-size: 1em;
                margin-bottom: 3em;
                margin-top: 0;
                padding-top: 0;
            }

            h1.text-mode {
                padding-left: 4.25em;
            }

            td {
                padding-right: .5em;
                padding-bottom: 10px;
                width: 1px;
                white-space: nowrap;
            }

            td.pt-size {
                text-align: right;
                font-family: humanst521_btbold;
                padding-right: 3em;
            }

            .red-quads {
                background-color: #FF4200;
            }

            .black-quads {
                background-color: #000000;
            }

        </style>
    </head>

    <body>

        <h1
"""

if MODE == "text":
    print " class='text-mode' "

print """
>Quadrats (CSS points)</h1>

        <table>

"""


all_point_sizes = (
    5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 36,
    40, 42, 48, 54, 56, 60, 72, 84, 90, 96, 108, 120, 126, 144, 168
)

body_sizes = (5, 6, 7, 8, 9, 10, 12, 14, 18, 24, 30, 36, 42, 48, 60, 72)
max_body_size_to_display = 42
offset = body_sizes[0]

rows = []
for ptsize in [x for x in body_sizes if x <= max_body_size_to_display]:
    row = []
    for cell in [i for i in range(offset, 169) if i in all_point_sizes]:
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

    if MODE == "text":
        print "<td class='pt-size'>{}</td>".format(body_sizes[row_idx])

    found = 0
    for td_idx, td in enumerate(row):
        if MODE == "text":
            print "<td>"
            print td if td else " "
            print "</td>"
        else:
            print '<td style="font-size: ' + str(body_sizes[row_idx]) + 'pt;">'
            if td:
                found += 1
                cell_pt_size = all_point_sizes[td_idx]
                multiple_size_use = (
                    cell_pt_size != body_sizes[row_idx] and
                    cell_pt_size in body_sizes
                )

                if multiple_size_use:
                    print "<span class='red-quads'>"
                else:
                    print "<span class='black-quads'>"
                for k in range(1, found + 1):
                    print "&#x2001;"
                print "</span>"
            else:
                print " "
            print "</td>"
    print "</tr>"

print "</table></body></html>"
