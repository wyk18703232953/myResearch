import math

def main(n):
    # Interpret n as the length of the list p
    if n < 2:
        # With fewer than 2 elements, original logic still prints 2
        # print(2)
        pass
        return

    # Deterministically generate p based on n
    # Example pattern: p[i] = i * 3
    p = [i * 3 for i in range(n)]

    q = []
    for i in range(len(p) - 1):
        q.append(abs(p[i + 1] - p[i]))
    count = 0
    for k in q:
        if k == 2 * d:
            count += 1
        elif k >= 2 * d:
            count += 2
    # print(count + 2)
    pass


# Since original code used an external d, we need a deterministic mapping from n to d.
# We redefine main to include d in a deterministic way while keeping the required signature.
def main(n):
    # Deterministically set d as a simple function of n (avoid zero)
    d = max(1, n // 3)

    if n < 2:
        # print(2)
        pass
        return

    p = [i * 3 for i in range(n)]

    q = []
    for i in range(len(p) - 1):
        q.append(abs(p[i + 1] - p[i]))

    count = 0
    for k in q:
        if k == 2 * d:
            count += 1
        elif k >= 2 * d:
            count += 2

    # print(count + 2)
    pass
if __name__ == "__main__":
    # Example deterministic run
    main(10)