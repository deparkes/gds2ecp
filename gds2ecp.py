import itertools
import csv

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

def getxy(gds_file):
    with open(gds_file) as f:
        for line in f:
            if line.startswith('XY: '):
                line = line.strip('XY: ')
                line = line.strip('\n')
                line = line.split(', ')
                return line
                
def to_coords(coords):
    """ Do this on a per-shape basis """
    # Separate out into xy coordinate pairs
    for chunk in coords:
        xy_pairs = grouper(chunk,2)
        xy_list = list(xy_pairs)
        return xy_list
                
def check_shape(coords):
    """ This works on a single set of 5 coordinate pairs to work out which
        ecp shape to use: either RECT, XPOLY, or YPOLY.
        Check for RECT, then XPOLY, then YPOLY.
        Have to be a bit careful, because of the slightly odd way ecp labels
        its x and y coordinates.
        """
    # Check for RECT
    # if y2 - y1 = y3-y1 & x2-x1 = x3-x1 then RECT
    
    # Check for xpoly
    # if y4 - y1 = 0 & y3 - y2 = 0 then XPOLY
        
    # Check for ypoly
    # if x4 - x1 = 0 & x3-x2 = 0 then YPOLY
    
    print(coords)
    
#print (getxy('writefield.txt'))

grouped = grouper(getxy('writefield.txt'),10)
#print list(grouped)

xy_coords = to_coords(list(grouped))
check_shape(xy_coords)

print(xy_coords)
