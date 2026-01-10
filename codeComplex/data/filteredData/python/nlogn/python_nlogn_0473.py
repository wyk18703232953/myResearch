def main(n):
    # 映射含义：
    # n -> 数组长度
    # m -> 与数组元素大小相关的上界（确定性构造）
    if n <= 0:
        print(0)
        return

    # 确定性生成 arr：长度为 n，元素值在 [1, n] 内循环分布
    arr = [(i % n) + 1 for i in range(n)]

    # m 为最大元素值，保持与原逻辑一致
    m = max(arr)

    res = [0] * (max(arr) + 1)
    for i in arr:
        res[i] += 1

    ans = 0
    for d in range(1, m + 1):
        temp = res[:]  # 代替 deepcopy，对一维列表足够
        cnt = 0
        for i in range(len(temp)):
            while temp[i] >= d:
                temp[i] -= d
                cnt += 1
        if cnt >= n:
            ans = max(ans, d)
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 规模进行实验
    main(1000)