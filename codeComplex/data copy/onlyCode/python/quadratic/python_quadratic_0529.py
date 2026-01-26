D = False

def hash(r,c):
    return str(r) + "-" + str(c)

def sol():
    R, C = [int(x) for x in input().split(" ")]
    m = []
    count = 0
    for _ in range(R):
        line = input()
        m.append(line)
        count += line.count("#")

    if D: print("Count:", count)

    lookup = {}
    for r in range(1, R-1):
        for c in range(1, C-1):

            if D: print("  row,col:", r, c)

            offset = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            lst = []
            fail = False

            # ensure all 8 adj cells are '#'
            # if so add to
            for o in offset:

                cell = (r + o[0], c + o[1])
                if D: print("  cell:", cell, m[cell[0]][cell[1]])
                h = hash(cell[0], cell[1])

                if m[cell[0]][cell[1]] == "#":
                    if (not h in lookup):
                        lst.append(h)

                else: # . found
                    fail = True
                    break

            if not fail:
                for item in lst:
                    lookup[item] = True
                count -= len(lst)

    return "YES" if count == 0 else "NO"

#for t in range(int(input())):
ans = sol()
print(ans)
