import itertools

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

def getxy(gds_file):
    with open(gds_file) as f:
        for line in f:
            if line.startswith('XY: '):
                line = line.strip('XY: ')
                line = line.split()
                return line
                
                
#print (getxy('writefield.txt'))

grouped = grouper(getxy('writefield.txt'),5)
print list(grouped)