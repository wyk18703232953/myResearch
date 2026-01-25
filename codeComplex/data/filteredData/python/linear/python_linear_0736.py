import sys
from collections import deque

def main(n):
    # n: number of initial elements in A, and also number of queries
    if n < 2:
        return

    # Deterministic construction of A and Q based on n
    # A: deque of n integers
    A = deque((i * 2 + 1) for i in range(n))

    # Q: list of n query integers
    limit = 10**5 + 1
    Q = []
    # first min(n, limit) queries: from 1 to ...
    upto = min(n, limit)
    Q.extend(range(1, upto + 1))
    # remaining queries, if any, exceed limit to exercise the periodic logic
    if n > upto:
        Q.extend(limit + 1 + i for i in range(n - upto))

    ANS = [0]

    # simulate first 10**5 + 1 operations (or fewer if not enough elements, but here n>=2)
    # this part does not depend on n beyond initial A
    for _ in range(10**5 + 1):
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

    for q in Q:
        if q <= 10**5 + 1:
            res = ANS[q]
            # ANS[q] is the pair (x, y)
            sys.stdout.write(f"{res[0]} {res[1]}\n")
        else:
            idx = (q - 10**5 - 2) % (n - 1)
            sys.stdout.write(f"{ANS0} {B[idx]}\n")


if __name__ == "__main__":
    # example deterministic call
    main(10)