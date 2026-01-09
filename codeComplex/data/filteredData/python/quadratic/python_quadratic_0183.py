def main(n):
    # Interpret n as the size of array a
    # Deterministically generate a and q, and queries
    a = [(i * 31 + 7) % (n + 3) for i in range(n)]
    Array = [a]

    # Build the XOR layers
    for _ in range(n - 1):
        aux = []
        last = Array[-1]
        for j in range(1, len(last)):
            aux.append(last[j - 1] ^ last[j])
        Array.append(aux)

    # Build the range-maximum structure over the XOR triangle
    for j in range(1, len(Array)):
        prev = Array[j - 1]
        curr = Array[j]
        for k in range(len(curr)):
            v = curr[k]
            m1 = prev[k]
            m2 = prev[k + 1]
            if m1 >= v and m1 >= m2:
                curr[k] = m1
            elif m2 >= v and m2 >= m1:
                curr[k] = m2

            else:
                curr[k] = v

    # Deterministically generate q and queries based on n
    # Let q be n (or at least 1)
    q = max(1, n)
    outputs = []
    for i in range(q):
        # Generate l, r with 1 <= l <= r <= n
        if n == 0:
            # Degenerate case, no valid queries
            outputs.append("0")
            continue
        l = (i % n) + 1
        # Ensure r >= l
        r = ((i * 2) % n) + 1
        if r < l:
            r = l
        # Access Array with the same logic as original
        idx_row = r - l
        idx_col = l - 1
        if 0 <= idx_row < len(Array) and 0 <= idx_col < len(Array[idx_row]):
            outputs.append(str(Array[idx_row][idx_col]))

        else:
            outputs.append("0")

    # Join outputs with newline to simulate the original printing behavior
    result = "\n".join(outputs)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)