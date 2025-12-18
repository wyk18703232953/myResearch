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

import collections

def numz(a,b):
    if a and b:
        if b > a:
            a,b=b,a
        d,m = divmod(a,b)
        return d + numz(b,m)
    else:
        return 0
    
if __name__ == '__main__':

    lines = read_lines(input_type=int)
    
    lines = lines[1:]
    for line in lines:
        print(numz(*line))
        
        
        