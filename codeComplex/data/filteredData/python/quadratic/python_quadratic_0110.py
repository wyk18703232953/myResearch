def vFlip(m):
    return [list(reversed(i)) for i in m]

def hFlip(m):
    return list(reversed(m))

def rotate(m):
    return [list(row) for row in zip(*reversed(m))]

def check(map1, map2):
    for _ in range(4):
        if map1 == map2:
            return True
        if vFlip(map1) == map2:
            return True
        if hFlip(map1) == map2:
            return True
        if vFlip(hFlip(map1)) == map2:
            return True
        map1 = rotate(map1)
    return False

def main(n):
    # n is the size of the square matrices (n x n)
    # Deterministic generation of map1 and map2
    # map1: pattern based on (i + j) % 2
    map1 = [['#' if (i + j) % 2 == 0 else '.' for j in range(n)] for i in range(n)]
    # map2: rotate(map1) twice (i.e., 180-degree rotation)
    map2 = rotate(rotate(map1))
    # Run the core logic
    res = check(map1, map2)
    # print('YES' if res else 'NO')
    pass
if __name__ == "__main__":
    main(10)