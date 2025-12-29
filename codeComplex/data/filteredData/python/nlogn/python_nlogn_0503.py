import random

def mergeSort(x):
    if len(x) > 1:
        mid = len(x) // 2
        L = x[:mid]
        R = x[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Merge section (descending order)
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                x[k] = L[i]
                i += 1
            else:
                x[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            x[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            x[k] = R[j]
            j += 1
            k += 1


def main(n):
    """
    n: number of (a, b) pairs to generate

    We emulate original logic:
    - Randomly generate (a, b)
    - m is a "limit" proportional to total a (for testing).
    """
    # Generate test data
    # a in [1, 100], b in [0, a] to keep differences non-negative sometimes
    pairs = []
    total = 0
    for _ in range(n):
        a = random.randint(1, 100)
        b = random.randint(0, a)
        pairs.append((a, b))
        total += a

    # Choose m so that sometimes reduction is needed, sometimes not
    # For example: m is between 50% and 90% of total
    if total == 0:
        m = 0
    else:
        m = random.randint(int(0.5 * total), int(0.9 * total))

    difference = []
    total = 0
    for a, b in pairs:
        total += a
        difference.append(a - b)

    mergeSort(difference)

    minimum = 0
    if total <= m:
        print("0")
        return

    for val in difference:
        minimum += 1
        total = total - val
        if total <= m:
            break

    if total > m:
        print("-1")
    else:
        print(minimum)


if __name__ == "__main__":
    # Example: run with n = 10
    main(10)