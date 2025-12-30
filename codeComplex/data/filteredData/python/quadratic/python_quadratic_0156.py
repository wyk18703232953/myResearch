import random

def solution(n, k, arr):
    ret = []
    grp = [None for _ in range(256)]
    for i in arr:
        if grp[i]:
            continue
        l = None
        for j in range(1, k):
            if i - j < 0:
                break
            if grp[i - j] is not None:
                l = i - j
                break
        if l is not None and grp[l] > i - k:
            grp[i] = grp[l]
        else:
            ll = l + 1 if l is not None else max(0, i - k + 1)
            for j in range(ll, i + 1):
                grp[j] = ll
    for i in arr:
        ret.append(grp[i])
    return ret


def main(n):
    # 生成测试数据：k 在 [1, n]，arr 为长度 n，元素在 [0, 255]
    if n <= 0:
        return []
    k = random.randint(1, max(1, n))
    arr = [random.randint(0, 255) for _ in range(n)]
    result = solution(n, k, arr)
    print('n =', n)
    print('k =', k)
    print('arr =', ' '.join(map(str, arr)))
    print('result =', ' '.join(map(str, result)))
    return result


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)