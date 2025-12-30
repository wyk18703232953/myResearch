import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组和一个区间下限 k
    # 这里假设数组元素为 0~100 的整数，k 在 1~n 之间
    arr = [random.randint(0, 100) for _ in range(n)]
    k = random.randint(1, n)

    # 前缀和数组（保持与原代码结构尽量一致）
    pf = [0] * (n + 1)
    pf[0] = arr[0]
    for i in range(1, n):
        pf[i] = pf[i - 1] + arr[i]

    ans = 0.0
    for i in range(n):
        for j in range(n):
            left = i
            right = j
            if right - left + 1 >= k:
                # 注意：left 可能为 0，原代码在这种情况下会访问 pf[-1]，
                # 这在 Python 中等价于访问最后一个元素，这里保持原逻辑不改动
                temp = pf[right] - pf[left - 1]
                ans = max(ans, temp / (right - left + 1))

    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)