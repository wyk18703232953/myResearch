import random

def main(n):
    # 生成测试数据
    # k 在 [1, n] 内随机取值
    k = random.randint(1, n)
    # 生成一个严格递增的数组 arr，长度为 n
    # 为方便，可生成随机步长并累加
    steps = [random.randint(1, 10) for _ in range(n)]
    arr = []
    cur = random.randint(0, 10)
    for s in steps:
        cur += s
        arr.append(cur)

    # 原逻辑开始
    k -= 1
    arr_new = sorted([arr[i + 1] - arr[i] for i in range(n - 1)], reverse=True)
    result = arr[-1] - arr[0] - sum(arr_new[:k])

    print("n =", n)
    print("k (original input) =", k + 1)
    print("arr =", arr)
    print("result =", result)


if __name__ == "__main__":
    # 示例调用：n 可以根据需要修改
    main(10)