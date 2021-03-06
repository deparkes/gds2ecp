# gds2ecp
Convert gds2 files to pat files for Xenos ECP CAD files.

Copyright 2015 
Duncan Parkes 
deparkes@gmail.com 


## Usage
Plan to have usage something like:
gds2ecp my_file.gds

which will output to stdout.

We can output to a file by using

gds2ecp my_file.gds > my_file.pat

in keeping with gds2txt.py script with gdsii package.

## Required Features
- strip shapes from gds file
- deals with repeated shapes in gds file
- Manual input of doses
- Fixed 500um write field

# Optional features
- Dose encoded in layer
- Dose calculator
- Design centering
- Generation of ctl file
- Multiple write field sizes

## Plan
- Heavy lifting of converting binary gds to ascii will be done by gdsii python package.
- Strip XY BOUNDARY data from gds file
- Split XY coords list into 5 coords to put into pat file components: RECT, XPOLY, YPOLY
- check which pat file shape each set of 5 coords should be
- Output correct format for pat files
- Figure out how to deal with repeated shapes
- Figure out how to divide gds boundaries into pat shapes

## Code features
- objects for individual patterns
- config parser
- opt parser 
- Also output ctl control 

## Notes
- Use something like: https://code.google.com/p/poly2tri/ to triangulate more complicated polygons. Not sure if this is the best way.
- A better way is probably to do something like this to break a polygon into 'primitives'. http://creativemachines.cornell.edu/papers/CSG96_Lipson.pdf
- This guide on python cad talks about primitives
- alpha hull: http://blog.thehumangeo.com/2014/05/12/drawing-boundaries-in-python/
http://nbviewer.ipython.org/github/dwyerk/boundaries/blob/master/concave_hulls.ipynb
http://sgillies.net/blog/1155/the-fading-shape-of-alpha/
=======
- ECP actually only breaks the gds boundary into XPOLY and RECT. So it should be possible to do something like: for each vertex of the polygon put a horizontal (constant x) line out in the positive and negative x direction. Keep going until it hits the edge of the polygon. Go to the next vertex and do the same.	

Determine if point is inside polygon:
http://www.ariel.com.au/a/python-point-int-poly.html
Or probably better, use shapely:
http://toblerity.org/shapely/manual.html#contains

http://stackoverflow.com/questions/6989100/sort-points-in-clockwise-order

I think the approach I am going for is this: http://en.wikipedia.org/wiki/Monotone_polygon
http://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain

Decomposition
http://sarielhp.org/teach/2004/b/24_partition_slides.pdf

### Trapezoidation:
https://books.google.co.uk/books?id=iYzYh1uWjbgC&lpg=PA75&ots=EDfydPmTQC&dq=polygon%20trapezoidation&pg=PA83#v=onepage&q=polygon%20trapezoidation&f=false
A fast trapezoidation technique for planar polygons: doi:10.1016/S0097-8493(01)00180-7

A universal trapezoidation algorithm for planar polygons: doi:10.1016/S0097-8493(99)00044-8

A simple and fast incremental randomized algorithm for computing trapezoidal decompositions and for triangulating polygons
https://www.cs.princeton.edu/courses/archive/fall05/cos528/handouts/A%20Simple%20and%20fast.pdf
doi:10.1016/0925-7721(91)90012-4