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
    # n 作为数组长度规模
    # k 随 n 确定性设置，限制在 1~10 之间
    if n <= 0:
        return
    k = max(1, min(10, n // 5 + 1))
    # 数组中的值限制在 0~255 之间
    # 使用简单算术构造，保证确定性
    arr = [(i * 7 + 3) % 256 for i in range(n)]
    res = solution(n, k, arr)
    # print(' '.join(map(str, res)))
    pass
if __name__ == "__main__":
    # 示例规模，可根据需要调整
    main(20)