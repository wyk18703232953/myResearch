def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        l = []; board = []
        for i in range(n):
            li = list(map(int, input().split()))
            board.append(li)
            for j in range(m):
                l.append((li[j], j))
        l.sort(key = lambda x : x[0], reverse = True)
        idxs = set()
        z = 0
        while len(idxs) < min(n, m):
            curr = l[z]
            idxs.add(curr[1])
            z += 1
        idxs = list(idxs)
        total = 0
        for i in range(n ** n):
            rotations = []; num = i
            for j in range(n - 1, -1, -1):
                nj = n ** j
                q = num // nj
                num -= q * nj
                rotations.append(q)
            subtotal = 0
            #print(board, idxs, rotations)
            for k in range(n):
                #print([board[(k + rotations[col]) % n][idxs[col]] for col in range(n)])
                subtotal += max(board[(k + rotations[col]) % n][idxs[col]] for col in range(min(n, m)))
            total = max(total, subtotal)
        print(total)
main()