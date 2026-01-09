def main(n):
    # Deterministic input generation based on n
    # a: string of digits length n, digits cycling 0-9
    # b: string of digits length n, digits descending from 9
    a = ''.join(str(i % 10) for i in range(n))
    b = ''.join(str((9 - i) % 10) for i in range(n))

    fre = [0] * 11
    c = False
    found = [False]  # to emulate early exit in a controlled way

    def DFS(aa, bb):
        nonlocal c
        if found[0]:
            return
        if int(aa) == len(a):
            # print(bb)
            pass
            found[0] = True
            return
        for i in range(9, -1, -1):
            if (fre[i] > 0 and i <= int(b[int(aa)])) or (fre[i] > 0 and c):
                fre[i] -= 1
                prev_c = c
                if i < int(b[int(aa)]):
                    c = True
                DFS(aa + 1, bb * 10 + i)
                fre[i] += 1
                c = prev_c

    if len(b) > len(a):
        x = sorted(a)
        # print(*x[::-1], sep='')
        pass

    else:
        for ch in a:
            fre[int(ch)] += 1
        DFS(0, 0)


if __name__ == "__main__":
    main(5)