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
                
def topat(coords):
    """ Do this on a per-shape basis """
    for chunk in coords:
        xy_pairs = grouper(chunk,2)
        print list(xy_pairs)
                
#print (getxy('writefield.txt'))

grouped = grouper(getxy('writefield.txt'),10)
#print list(grouped)

topat(list(grouped))

