def main(n):
    # n is the number of nodes in a tree
    # Generate a deterministic tree with n nodes:
    # For 1 <= i < n, connect i with i+1 (a simple path)
    if n < 2:
        # For n < 2, the original logic expects at least n=2
        # We handle n=1 as a degenerate case with no edges
        # print("No")
        pass
        return

    edges = [[i, i + 1] for i in range(1, n)]
    deg = [0] * n

    if n == 2:
        # print("Yes")
        pass
        # print(1)
        pass
        # print("1 2")
        pass
        return

    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    ix = deg.index(max(deg))

    if deg[ix] < 3 or deg.count(1) + deg.count(2) == n - 1:
        # print("Yes")
        pass
        # print(deg.count(1))
        pass
        for i in range(n):
            if deg[i] == 1:
                # print(i + 1, ix + 1)
                pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    # Example: run main with a chosen scale n
    main(10)