
def getxy(gds_file):
    with open(gds_file) as f:
        for line in f:
            if line.startswith('XY: '):
                line = line.strip('XY: ')
                print(line)
                

getxy('writefield.txt')