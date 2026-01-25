import sys
from itertools import accumulate
import copy

def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministic generation of n, m, k, and A based on input scale n
    N = n
    M = max(1, min(5, N))  # m between 1 and 5, but not larger than N
    K = 3                  # fixed positive integer

    # Generate array A of length N deterministically
    A = [(i * 2 + 1) % 10 for i in range(N)]

    n_local = N
    m_local = M
    k_local = K

    ANS = 0

    for i in range(m_local):
        B = copy.deepcopy(A)

        for j in range(i, n_local, m_local):
            B[j] -= k_local

        SUM = list(accumulate(B))
        SUMMIN = [float("inf")] * n_local + [0]

        if i == 0:
            SUMMIN[0] = 0

        for j in range(max(1, i), n_local):
            if j % m_local == i % m_local:
                SUMMIN[j] = min(SUMMIN[j - 1], SUM[j - 1])
            else:
                SUMMIN[j] = SUMMIN[j - 1]

        for j in range(i, n_local):
            ANS = max(ANS, SUM[j] - SUMMIN[j])

    print(ANS)


if __name__ == "__main__":
    # Example deterministic call; change 10 to other n for experiments
    main(10)