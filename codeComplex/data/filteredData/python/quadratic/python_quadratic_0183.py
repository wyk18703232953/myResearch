import sys

def main(n):
    # Deterministic data generation based on n
    if n <= 0:
        return
    a = [(i * 3 + 1) % (n + 7) for i in range(n)]
    Array = [a]

    # Build XOR levels
    for _ in range(n - 1):
        aux = []
        last = Array[-1]
        for j in range(1, len(last)):
            aux.append(last[j - 1] ^ last[j])
        Array.append(aux)

    # Propagate maximums
    for j in range(1, len(Array)):
        row = Array[j]
        prev = Array[j - 1]
        for k in range(len(row)):
            row[k] = max(row[k], prev[k], prev[k + 1])

    # Deterministic queries based on n
    q = n
    results = []
    for i in range(q):
        l = (i % n) + 1
        r = n
        if l <= r:
            results.append(str(Array[r - l][l - 1]))

        else:
            results.append("0")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main(5)