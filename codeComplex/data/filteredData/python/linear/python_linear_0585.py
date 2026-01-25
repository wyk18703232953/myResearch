import sys

C = 10**9 + 7

def main(n):
    # n controls the length of the binary list and number of queries
    if n <= 0:
        return

    # Generate deterministic "n q" where q = n
    q = n

    # Generate deterministic binary string of length n (no newline)
    # Pattern: lst[i] = i % 2 (0101...)
    lst = [i % 2 for i in range(n)]

    # Build prefix counts of zeros and ones
    new_lst = [(0, 0)]
    for i in lst:
        if i == 0:
            new_lst.append((new_lst[-1][0] + 1, new_lst[-1][1]))
        else:
            new_lst.append((new_lst[-1][0], new_lst[-1][1] + 1))

    # Precompute powers of 2 modulo C up to n
    ls = [1]
    for i in range(n):
        ls.append(ls[-1] * 2 % C)

    # Deterministically generate q queries (l, r)
    # For k-th query (0-based): l = k % n + 1, r = n
    # Ensures 1 <= l <= r <= n
    for k in range(q):
        l = k % n + 1
        r = n
        zeros = new_lst[r][0] - new_lst[l - 1][0]
        ones = new_lst[r][1] - new_lst[l - 1][1]
        total = zeros + ones
        print((ls[total] - ls[zeros]) % C)


if __name__ == "__main__":
    # Example deterministic call
    main(10)