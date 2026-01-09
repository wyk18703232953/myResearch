from collections import deque

def main(n):
    # n controls the size of the initial deque A and the number of queries q
    if n < 2:
        n = 2

    # Deterministic construction of initial deque A with n elements
    # Example pattern: A[i] = (i * 2 + 1) % (3 * n) + 1
    A = deque(((i * 2 + 1) % (3 * n) + 1) for i in range(n))

    # Deterministic construction of q queries
    # Let q = n; queries cover both <= 1e5+1 and > 1e5+1
    q = n
    base = 10**5 + 1
    Q = []
    for i in range(q):
        if i % 2 == 0:
            Q.append((i % (base + 1)) + 1)   # in [1, base+1]

        else:
            Q.append(base + 2 + i)           # > base+1

    ANS = [0]

    limit = 10**5 + 1
    # Ensure we have enough elements in A for popping pairs
    # Original logic assumes initial n from input is large enough, keep same loop
    for _ in range(limit):
        x = A.popleft()
        y = A.popleft()

        ANS.append((x, y))

        if x > y:
            A.appendleft(x)
            A.append(y)

        else:
            A.appendleft(y)
            A.append(x)

    ANS0 = A[0]
    B = list(A)[1:]

    for qq in Q:
        if qq <= limit + 1:
            # print(*ANS[qq])
            pass

        else:
            # print(ANS0, B[(qq - limit - 2) % (n - 1)])
            pass
if __name__ == "__main__":
    main(10**5)