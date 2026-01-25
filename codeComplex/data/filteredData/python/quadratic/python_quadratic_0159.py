def main(n):
    # Interpret n as number of elements and parameter k
    # Ensure at least 1 element
    if n <= 0:
        n = 1

    # Define k deterministically from n, but at least 1
    k = max(1, n // 3)

    # Generate a deterministic list ps of length n with values in [0, 255]
    # Use a simple arithmetic pattern to stay within 0..255
    ps = [(i * 7 + 3) % 256 for i in range(n)]

    mapping = [-1 for _ in range(256)]

    res = []
    for p in ps:
        if mapping[p] == -1:
            j = p - k + 1
            while j < 0 or (mapping[j] != -1 and mapping[j] + k <= p):
                j += 1
            for i in range(j, p + 1):
                mapping[i] = j
        res.append(mapping[p])

    print(" ".join(map(str, res)))


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)