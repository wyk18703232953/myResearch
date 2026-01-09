from queue import Queue
import datetime

def main(n):
    # Deterministically generate n, m, k, ints based on input scale n
    # Map n to grid size and number of pairs
    rows = n
    cols = n
    k = max(1, n // 2)  # number of integers, must be even for pairs

    # Ensure k is even so that we can form (x, y) pairs
    if k % 2 == 1:
        k += 1

    # Generate k integers deterministically within grid bounds [1, n]
    ints = [((i * 2 + 3) % n) + 1 for i in range(k)]

    # If by construction some values become 0 (shouldn't with formula above), fix them
    ints = [v if v != 0 else 1 for v in ints]

    n_val = rows
    m_val = cols

    pairs = []
    for i in range(0, len(ints), 2):
        x = ints[i]
        y = ints[i+1]
        pairs.append((x, y))

    last_tree = (1, 1)
    maxd = 0
    mult = m_val * n_val
    for i in range(1, n_val+1):
        for j in range(1, m_val+1):
            md = mult
            for pair in pairs:
                x, y = pair
                d = abs(i-x) + abs(j-y)
                md = min(md, d)
            if md > maxd:
                last_tree = (i, j)
                maxd = md

    # For experimentation, just print the result instead of writing files
    # print(f"{last_tree[0]} {last_tree[1]}")
    pass
    return last_tree


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)