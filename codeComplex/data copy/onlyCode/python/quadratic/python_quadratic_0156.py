def solution(n, k, arr):
    ret = []
    grp = [None for _ in range(256)]
    for i in arr:
        if grp[i]:
            continue
        l = None
        j = 1
        for j in range(1, k):
            if i - j < 0:
                break
            if grp[i - j] is not None:
                l = i - j
                break
        if l is not None and grp[l] > i - k:
            grp[i] = grp[l]
        else:
            ll = l + 1 if l else max(0, i - k + 1)
            for j in range(ll, i + 1):
                grp[j] = ll
    for i in arr:
        ret.append(grp[i])
    return ret


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(' '.join(map(str, solution(n, k, arr))))
