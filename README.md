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