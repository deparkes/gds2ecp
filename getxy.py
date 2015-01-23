with open('writefield.txt') as f:
    for line in f:
        if line.startswith('XY: '):
            line = line.strip('XY: ')
            print(line)