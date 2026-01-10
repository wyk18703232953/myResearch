def bin_ser(arr, curr):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= curr:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


def experiment_logic(n, q, arr, brr):
    su = sum(arr)
    curr = 0
    for i in range(1, n):
        arr[i] = arr[i] + arr[i - 1]
    outputs = []
    for b in brr:
        curr += b
        pos = n - bin_ser(arr, curr) - 1
        if pos == 0:
            pos = n
        outputs.append(pos)
        if curr >= su:
            curr = 0
    return outputs


def main(n):
    # 映射规则：
    # n 为整体规模，将其拆为：
    #   数组长度 N = n
    #   查询次数 Q = n
    N = n
    Q = n

    # 构造确定性数据
    # arr 为严格递增正整数，用于前缀和逻辑
    # 例如：arr[i] = i + 1
    arr = [i + 1 for i in range(N)]

    # brr 为每次“攻击量”，构造有重复和变化：
    # 使用简单算术结构，完全确定
    # 例如：brr[i] = (i % N) + 1
    if N == 0:
        brr = []
    else:
        brr = [(i % N) + 1 for i in range(Q)]

    outputs = experiment_logic(N, Q, arr, brr)

    # 为了在时间复杂度实验中有可观测输出，这里打印结果
    for v in outputs:
        print(v)


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的规模做实验
    main(10)