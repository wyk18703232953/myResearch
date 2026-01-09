def main(n):
    if n < 1:
        # print("NO")
        pass
        return
    t = [[] for _ in range(n + 1)]
    # Deterministic tree construction:
    # For each node i from 2 to n, its parent is i//2 (classic heap-like tree)
    for i in range(2, n + 1):
        v = i // 2
        t[v].append(i)

    flag = True
    for l in t:
        if l:
            cnt = 0
            for ele in l:
                if t[ele] == []:
                    cnt += 1
            if cnt < 3:
                flag = False
                break

    if flag:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)