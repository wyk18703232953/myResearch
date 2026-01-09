def count(audrey, imba, banget):
    return (imba - audrey - 1) % (banget - 1)

def main(n):
    # n controls both array size and query count
    if n < 2:
        n = 2

    # Deterministic generation of n (array size) and q (number of queries)
    N = n
    q = n

    # Generate L: length N, ensure a maximum somewhere in the middle
    # L[i] = (i * 2 + 3) % (N + 7) + 1, deterministic and varied
    L = [((i * 2 + 3) % (N + 7)) + 1 for i in range(N)]
    # Ensure a clear maximum at a fixed position (for determinism in indexmax)
    max_pos = N // 3
    if max_pos >= N:
        max_pos = N - 1
    L[max_pos] = max(L) + 5
    maxi = max(L)
    indexmax = L.index(maxi)

    P = []
    # simulate the process to fill P
    from collections import deque
    dq = deque(L)
    for _ in range(indexmax):
        P.append((dq[0], dq[1]))
        if dq[0] < dq[1]:
            dq.append(dq.popleft())

        else:
            x = dq[1]
            del dq[1]
            dq.append(x)
    Y = tuple(list(dq)[1:])

    # Deterministic generation of q queries m
    # m ranges from 1 up to something around N+q to cover both branches
    queries = [1 + (i * 3) % (N + q) for i in range(q)]

    out_lines = []
    for m in queries:
        if m <= indexmax:
            out_lines.append(str(P[m - 1][0]) + " " + str(P[m - 1][1]))

        else:
            out_lines.append(str(maxi) + " " + str(Y[count(indexmax, m, N)]))
    # print("\n".join(out_lines))
    pass
if __name__ == "__main__":
    main(10)