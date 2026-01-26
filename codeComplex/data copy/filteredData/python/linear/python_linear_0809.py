def main(n):
    # Interpret n as the number of special positions (m)
    # Keep k as a fixed deterministic divider, and n (first input) derived from m so the algorithm remains meaningful.
    if n <= 0:
        # print(0)
        pass
        return

    m = n
    k = 3  # fixed divider, deterministic
    total_count = m + 10  # ensure n in original sense is >= m

    # Deterministic, strictly increasing "special" positions within [1, total_count]
    # Ensure special[i] >= i+1 and strictly increasing.
    special = [i + 1 + (i // 2) for i in range(m)]

    numOn = 0
    numOps = 0
    while numOn < m:
        numOps += 1
        op = ((special[numOn] - numOn - 1) // k) * k + k + numOn + 1
        while numOn < m and special[numOn] < op:
            numOn += 1
    # print(numOps)
    pass
if __name__ == "__main__":
    # Example: run with a few different scales
    for n in [1, 5, 10, 50]:
        main(n)