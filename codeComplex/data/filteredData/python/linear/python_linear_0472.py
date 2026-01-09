def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return 0

    # Deterministic generation of C and A for size n
    # C: costs, positive integers
    C = [(i * 7 + 3) % 1000000007 + 1 for i in range(n)]

    # A: permutation-like mapping with possible cycles
    # Ensure indices are in 0..n-1
    A = [((i * 3 + 1) % n) for i in range(n)]
    A = [a for a in A]  # already zero-based

    visit = [False] * n
    loops = []
    for i in range(n):
        if not visit[i]:
            s = [i]
            temp = set()
            temp.add(i)
            flag = False
            while s:
                v = s.pop()
                if visit[A[v]]:
                    break
                if A[v] in temp:
                    flag = True
                    p = A[v]
                    break

                else:
                    s.append(A[v])
                    temp.add(A[v])
            if flag:
                loop = [p]
                nv = A[p]
                while nv != p:
                    loop.append(nv)
                    nv = A[nv]
                loops.append(loop)
            for v in temp:
                visit[v] = True

    ans = 0
    for l in loops:
        m = 10**18
        for i in l:
            if C[i] < m:
                m = C[i]
        ans += m

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)