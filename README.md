# froshaug-norms
Kinross describes the &#8216;visual tables&#8217; of Anthony Froshaug&#8217;s
_Typographic norms_ as &#8216;beautiful constellations; mysterious reports on typography&#8217;.
Having appreciated that beauty for a long time, we wanted to lessen the mystery
a bit to understand better what was happening under the hood. So this is a modest
attempt at doing that by writing a computer program to render one of the
iterations
[in the browser](http://i-s-o-g-r-a-m.github.io/froshaug-norms/).

Of the choices available, &#8216;Quadrats (Anglo-American)&#8217; seemed
like the right one to select. It&#8217;s the coolest-looking
and, from an, uhhh, Anglo-American perspective, is the most familiar in terms
of body sizes. (We presume an equivalency between Anglo-American points
and CSS/browser points.)

The recipe for generating the data that, in turn, yields the output we want,
is as follows:

* the x-axis (unlabeled, even in the numerical rendition, since the labeling
there would be redundant) ranges across what appears to be a complete set of
known standard sizes, starting at 5 and going up to 168

* the y-axis (helpfully labeled in the numerical rendition of the table) also starts
at 5, but includes only a subset of -- and we do not know the right term
here -- the most commonly-used sizes: 5, 6, 7, 8, 9, 10, 12, 14, 18, 24, 30, 36, 42.
(48, 60, 72 are also part of this set, but they are omitted, possibly because
quads wouldn&#8217;t be available at those large sizes; other types of furniture
might instead have been used at that point, we guess).

* iterating over the y-axis sizes, from 5 to 42, we construct rows containing
cells. Each row will have exactly four quads in it, probably because there
would be four types of quads available: (1-)quads, 2-quads, 3-quads, 4-quads.

* a quad is placed in a cell when the following condition is true: 
the x-axis size is the same as the y-axis size _or_ the x-axis size is
evenly divisible by the y-axis size. To be explicit: the width of the quad
placed in the cell is equivalent to the point size of the current
position on the x-axis; the height is equivalent to that of the y-axis.

* a quad is determined to be a multiple-size-use quad, thereby receiving the
alternate color in the visual table, if it is (1) not a 1-quad and (2) has
a width equal to one of the commonly-used sizes enumerated above.
