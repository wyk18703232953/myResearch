def vFlip(m):
    return [list(reversed(row)) for row in m]

def hFlip(m):
    return list(reversed(m))

def rotate(m):
    return [list(row) for row in zip(*reversed(m))]

def generate_maps(n):
    # Generate a deterministic n x n map1 of characters
    map1 = [[chr(65 + (i + j) % 26) for j in range(n)] for i in range(n)]

    # For map2, choose a deterministic transformation of map1 based on n
    t = n % 8
    if t == 0:
        map2 = [row[:] for row in map1]
    elif t == 1:
        map2 = vFlip(map1)
    elif t == 2:
        map2 = hFlip(map1)
    elif t == 3:
        map2 = vFlip(hFlip(map1))
    elif t == 4:
        map2 = rotate(map1)
    elif t == 5:
        map2 = rotate(rotate(map1))
    elif t == 6:
        map2 = vFlip(rotate(map1))
    else:  # t == 7
        map2 = hFlip(rotate(map1))

    return map1, map2

def check(map1, map2):
    m = [row[:] for row in map1]
    for _ in range(4):
        if m == map2:
            return True
        if vFlip(m) == map2:
            return True
        if hFlip(m) == map2:
            return True
        if vFlip(hFlip(m)) == map2:
            return True
        m = rotate(m)
    return False

def main(n):
    if n <= 0:
        return
    map1, map2 = generate_maps(n)
    result = 'YES' if check(map1, map2) else 'NO'
    # print(result)
    pass
if __name__ == "__main__":
    main(5)