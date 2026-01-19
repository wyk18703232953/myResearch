import sys

def generate_state(N, M, base=1000000000):
    # Deterministic matrix generation based on N and M
    # Each entry is positive to allow meaningful threshold binary search
    state = []
    for i in range(N):
        row = []
        for j in range(M):
            # Simple deterministic formula, values within [1, base]
            val = ((i + 1) * (j + 2) * (i + j + 3)) % base
            if val == 0:
                val = 1
            row.append(val)
        state.append(row)
    return state

def solve_from_state(state):
    N = len(state)
    if N == 0:
        return -1, -1
    M = len(state[0]) if state[0] else 0

    Ans = {}
    l = -1
    r = 10**9 + 1
    full_mask = (1 << M) - 1

    while r - l > 1:
        m = (l + r) // 2
        T = {}
        for j, S in enumerate(state):
            bit = 0
            for i, s in enumerate(S):
                if s >= m:
                    bit += 1 << i
            T[bit] = j

        ok = False
        for bit1 in range(1 << M):
            for bit2 in range(1 << M):
                if (bit1 | bit2) == full_mask and bit1 in T and bit2 in T:
                    ok = True
                    Ans[m] = [T[bit1], T[bit2]]
                    break
            if ok:
                break

        if ok:
            l = m
        else:
            r = m

    if l in Ans:
        return Ans[l][0] + 1, Ans[l][1] + 1
    return -1, -1

def main(n):
    # Map n to matrix dimensions
    # Choose M proportional to log(n+1) (at least 1)
    if n <= 0:
        N, M = 1, 1
    else:
        M = max(1, (n.bit_length() + 1) // 2)
        N = max(1, n // max(1, M))

    state = generate_state(N, M)
    a, b = solve_from_state(state)
    print(a, b)

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)