import random

def main(n):
    # 生成测试数据：n 和 p
    # 这里假定 p 为一个较大的正整数，且 p > 0
    p = random.randint(1, 10**9)
    # 生成数组 arr，元素为随机整数
    arr = [random.randint(0, 10**9) for _ in range(n)]

    # 原逻辑开始
    prefsums = [arr[0]]
    for i in range(1, n):
        prefsums.append(prefsums[i - 1] + arr[i])

    allsum = sum(arr)

    if len(arr) == 2:
        print(arr[0] % p + arr[1] % p)
        return

    res = []
    for i in range(1, n - 1):
        res.append((prefsums[i] % p) + ((allsum - prefsums[i]) % p))

    print(max(res))


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改
    main(5)