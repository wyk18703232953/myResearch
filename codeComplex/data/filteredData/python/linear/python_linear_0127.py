def if_spruce(n, l, s):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if i not in s:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if i in s and d[i] < 3:
            return "No"
    return "Yes"

def main(n):
    if n < 2:
        # For n < 2, original loop "for _ in range(n-1)" has no iterations,
        # and the input sequence is effectively just the initial l = [0, 0].
        l = [0, 0]

    else:
        # Deterministically generate a tree parent array for nodes 2..n.
        # Use 1 as parent for all nodes to maximize leaves.
        l = [0, 0]
        for i in range(2, n + 1):
            l.append(1)
    s = set(l)
    result = if_spruce(n, l, s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)