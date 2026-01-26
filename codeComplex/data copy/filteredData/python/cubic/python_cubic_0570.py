def main(n):
    # Deterministic generation of two digit lists a and b of length n
    # Digits cycle from 0 to 9
    a = [i % 10 for i in range(n)]
    b = [(n - i - 1) % 10 for i in range(n)]

    from copy import deepcopy

    cnt1 = [0] * 10
    cnt2 = [0] * 10
    ans = []
    if len(a) != len(b):
        # print(''.join(map(str, sorted(a, reverse=True))))
        pass
        return
    for i in range(len(b) + 1):
        ok = 1
        tmp = deepcopy(a)
        for j in range(i):
            if b[j] in tmp:
                tmp.pop(tmp.index(b[j]))

            else:
                ok = 0
                break
        if not ok:
            continue
        pls = -1
        ind = -1
        for j in range(len(tmp)):
            if tmp[j] < b[i]:
                if tmp[j] > pls:
                    ind = j
                    pls = tmp[j]
        if pls == -1 and len(tmp) != 0:
            continue

        else:
            if len(tmp) > 0:
                tmp.pop(ind)
            if i == len(b):
                ans.append(''.join(map(str, b[:i])))

            else:
                ans.append(''.join(map(str, b[:i])) + str(pls) + ''.join(map(str, sorted(tmp, reverse=True))))
    # print(max(ans))
    pass
if __name__ == "__main__":
    main(10)