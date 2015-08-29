from __future__ import print_function
import sys


MODE = "text" if "text" in sys.argv else "spacing"


def make_norms():
    print("""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title>Typographic norms</title>

            <link rel="stylesheet" href="css/animate.min.css">

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
                    font-size: 1.3em;
                    padding: 1em .75em 1em .75em;
    """)

    if MODE == "text":
        print('font-family: humanst521_btroman, sans-serif;')
    else:
        print('font-family: "Times New Roman", Times, Georgia, serif;')
    print("""
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
    """)
    if MODE == "text":
        print(" padding-bottom: 1em;")
    else:
        print(" padding-bottom: .7em;")
    print("""
                    width: 1px;
                    white-space: nowrap;
                }

                td.pt-size {
                    text-align: right;
                    font-family: humanst521_btbold;
                    padding-right: 3em;
                }

                .red-quad {
                    background-color: #FF4200;
                }

                .black-quad {
                    background-color: #000000;
                }

            </style>
        </head>

        <body>

            <h1
    """)

    if MODE == "text":
        print(" class='text-mode' ")

    print("""
    >Quadrats (CSS points)</h1>

            <table>

    """)


    ALL_PT_SIZES = (
        5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32,
        36, 40, 42, 48, 54, 56, 60, 72, 84, 90, 96, 108, 120, 126, 144, 168)

    STANDARD_SIZES = (5, 6, 7, 8, 9, 10, 12, 14, 18, 24, 30, 36, 42, 48, 60, 72)

    MAX_STANDARD_SIZE_TO_DISPLAY = 42


    rows = []
    for ptsize in [x for x in STANDARD_SIZES if x <= MAX_STANDARD_SIZE_TO_DISPLAY]:
        row = []
        for cell in [i for i in range(STANDARD_SIZES[0], ALL_PT_SIZES[-1] + 1) if i in ALL_PT_SIZES]:
            if len([i for i in row if i is not None]) == 4:
                row.append(None)
                continue
            if ptsize == cell or (cell % ptsize == 0):
                row.append(cell)
            else:
                row.append(None)
        assert len([x for x in row if x is not None]) == 4
        rows.append(row)

    for row_idx, row in enumerate(rows):
        print("<tr class='unpopulated'>")
        if MODE == "text":
            print("<td class='pt-size'>{}</td>".format(STANDARD_SIZES[row_idx]))
        for td_idx, td in enumerate(row):
            if MODE == "text":
                print("<td>{}</td>".format(td or " "))
            else:
                print("<td>")
                if not td:
                    print(" ")
                else:
                    cell_pt_size = ALL_PT_SIZES[td_idx]
                    multiple_size_use = (
                        cell_pt_size != STANDARD_SIZES[row_idx] and
                        cell_pt_size in STANDARD_SIZES
                    )
                    quad_class = 'red-quad' if multiple_size_use else 'black-quad'
                    print("<div class='quad {}' style='display: none; width: {}pt; height: {}pt;'/>".format(
                        quad_class, cell_pt_size, str(STANDARD_SIZES[row_idx]))
                    )
                print("</td>")
        print("</tr>")

    print("</table>")
    print('<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>')
    print('<script src="js/norms.js"></script>')
    print("</body></html>")


if '__main__' == __name__:
    make_norms()
