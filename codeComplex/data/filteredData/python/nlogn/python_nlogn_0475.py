def main(n):
    # 映射含义：
    # n -> 数组长度
    # m -> 与 n 同规模，便于可规模化实验
    if n <= 0:
        return 0

    # 确定性生成输入数据
    m = n
    arr = [i % (n // 2 + 1) for i in range(n)]
    # 至少保证有正的最大值，避免 max(arr) 为 0 时数组过小
    if all(x == 0 for x in arr):
        arr[0] = 1

    res = [0] * (max(arr) + 1)
    for i in arr:
        res[i] += 1

    ans = 0
    for d in range(1, m + 1):
        temp = res[:]  # 替代 deepcopy，等价于原逻辑
        cnt = 0
        for i in range(len(temp)):
            while temp[i] >= d:
                temp[i] -= d
                cnt += 1
        if cnt >= n:
            ans = max(ans, d)
    return ans


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    # print(main(10))
    pass