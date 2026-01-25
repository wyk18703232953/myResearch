import sys

def main(n):
    # Deterministically generate C and A based on n
    # C: costs, positive and varied
    C = [(i * 37 + 13) % (10**6) + 1 for i in range(n)]
    # A: permutation-like structure with some cycles
    A = [(i * 2 + 3) % n for i in range(n)]

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
            m = min(m, C[i])
        ans += m
    print(ans)
    return ans

if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)