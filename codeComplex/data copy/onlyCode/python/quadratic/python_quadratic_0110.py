n = int(input())
map1 = [list(input()) for i in range(n)]
map2 = [list(input()) for i in range(n)]

def vFlip (m):
    return([list(reversed(i)) for i in m])
    
def hFlip(m):
    return(list(reversed(m)))
    
def rotate(m):
    return(list(zip(*reversed(m))))
 
def check(): 
    global map1
    for i in range(4):
        if map1 == map2:
            return(True)
        if vFlip(map1)==map2:
            return(True)
        if hFlip(map1)==map2:
            return(True)
        if vFlip(hFlip(map1))==map2:
            return(True)
        map1 = rotate(map1)
    return(False)
    
print('YES' if check() else 'NO')