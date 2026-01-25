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


def main(n):
    if n <= 0:
        return
    k = max(1, n // 4)
    k = min(k, 255)
    arr_len = min(n, 256)
    if arr_len == 0:
        return
    step = max(1, 256 // arr_len)
    arr = [(i * step) % 256 for i in range(arr_len)]
    res = solution(arr_len, k, arr)
    print("n =", n)
    print("k =", k)
    print("len(arr) =", arr_len)
    print("arr =", " ".join(map(str, arr)))
    print("res =", " ".join(map(str, res)))


if __name__ == "__main__":
    main(10)