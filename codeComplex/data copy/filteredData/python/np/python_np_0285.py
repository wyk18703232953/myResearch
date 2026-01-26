import sys

def main(n):
    # n: tree size parameter, we map it to (n_nodes, q, sequence length)
    if n <= 0:
        return

    # Determine tree size and query count deterministically from n
    # Ensure n_nodes is odd and >= 1
    n_nodes = 2 * n + 1
    q = max(1, n)  # number of queries

    top = len(bin(n_nodes >> 1)) - 2
    ans = [1] * q

    # Deterministically generate initial node v for each query
    # v in [1, n_nodes], odd numbers only (valid nodes in this tree representation)
    # Also generate a deterministic command string s for each query
    # Pattern cycles through 'U', 'L', 'R'
    cmds = ['U', 'L', 'R']

    for i in range(q):
        # v: choose odd numbers in range [1, n_nodes], wrap by modulo
        # index from 0..(n_nodes//2), then map to 2*k+1
        k = i % ((n_nodes + 1) // 2)
        v = 2 * k + 1

        # command length grows slowly with n so total work is O(n^2) in worst case
        cmd_len = max(1, (i % (top + 1)) + 1)
        s = ''.join(cmds[(i + j) % 3] for j in range(cmd_len))

        if n_nodes == 1:
            ans[i] = v
            continue

        # find highest set bit position h
        for h in range(top + 1):
            if v & (1 << h):
                break

        for c in s:
            if (h == top and c == 'U') or (h == 0 and c != 'U'):
                continue
            if c == 'U':
                v -= 1 << h
                h += 1
                v |= 1 << h
            elif c == 'L':
                v -= 1 << h
                h -= 1
                v |= 1 << h
            else:
                h -= 1
                v |= 1 << h

        ans[i] = v

    # Output the results
    out = '\n'.join(str(x) for x in ans)
    sys.stdout.write(out + '\n')


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)