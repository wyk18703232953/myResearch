def main(n):
    if n <= 1:
        # print("Yes")
        pass
        return

    # Deterministically generate edges for a star-like structure:
    # nodes 2..n all point to node 1
    d, l, m, a = [0] * (n + 1), [0] * 2, [0] * (n + 1), 0
    for idx in range(2, n + 1):
        a = 1
        l.append(a)
        m[a] += 1

    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1

    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            # print("No")
            pass
            break

    else:
        # print("Yes")
        pass
if __name__ == "__main__":
    main(10)