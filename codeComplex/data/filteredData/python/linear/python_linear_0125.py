def if_Spruce(n, l, m):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            return "No"
    return "Yes"


def build_tree_parents(n):
    # Deterministic parent generation: for i>=2, parent is i//2
    l = [0, 0]
    m = [0] * (n + 1)
    for i in range(2, n + 1):
        p = i // 2
        l.append(p)
        m[p] += 1
    return l, m


def main(n):
    if n < 1:
        return ""
    l, m = build_tree_parents(n)
    result = if_Spruce(n, l, m)
    print(result)
    return result


if __name__ == "__main__":
    main(10)