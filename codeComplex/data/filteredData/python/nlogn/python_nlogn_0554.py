def main(n):
    # Ensure n is at least 1
    if n < 1:
        return

    # Deterministically generate a tree with n nodes
    # For i in [2..n], connect i with i//2 (a rooted tree with root 1)
    size = 2 * n + 1
    fst = [0] * size
    nxt = [0] * size
    lst = [0] * size
    des = [0] * size
    cnt = 0

    def add(u, v):
        nonlocal cnt
        cnt += 1
        if fst[u] == 0:
            fst[u] = cnt
        else:
            nxt[lst[u]] = cnt
        lst[u] = cnt
        des[cnt] = v

    for i in range(2, n + 1):
        u = i // 2
        v = i
        add(u, v)
        add(v, u)

    # Deterministically generate permutation a of [1..n]
    # Use simple transformation: reverse order
    a = [i for i in range(n, 1, -1)] + [1]

    deep = [0] * (n + 1)
    deep[1] = 1
    now, res = 1, 1
    Ans = 0

    for i in range(n):
        if deep[a[i]] == 0:
            Ans = 1
            break
        elif deep[a[i]] < now:
            Ans = 1
            break
        else:
            b = fst[a[i]]
            res += 1
            while b > 0:
                if deep[des[b]] == 0:
                    deep[des[b]] = res
                b = nxt[b]
            now = deep[a[i]]

    if Ans == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)