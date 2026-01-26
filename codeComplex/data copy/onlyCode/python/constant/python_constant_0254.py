from sys import stdin
 
def read_lines(sep=' ', input_type=None):
    #list of rows
    _lines = stdin.readlines()
    cast = input_type is not None
    lines = []
    for line in _lines:
        line = line[:-1].split(sep)
        if cast:
            line = [input_type(x) for x in line]
        lines.append(line)
    return lines

import math
        
if __name__ == '__main__':
 
    lines = read_lines(input_type=int)
    
    #t = lines[0]
    #lines = lines[1:]
    
    n,m = lines[0][0], lines[1][0]
    
    if n <= math.log2(m):
        print(m % (2**n))
    else:
        print(m)
        