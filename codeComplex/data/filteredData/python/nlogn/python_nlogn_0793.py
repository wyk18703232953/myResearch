import random

def main(n):
    # 1. 生成测试数据
    # 随机选取 k，1 <= k <= n
    k = random.randint(1, n)
    # 生成一个长度为 n 的非降序数组 a
    a = sorted(random.randint(0, 1000) for _ in range(n))

    # 2. 原逻辑实现
    t = []
    for i in range(1, n):
        t.append(a[i] - a[i - 1])
    t.sort()
    result = sum(t[:n - k])

    # 返回结果和测试数据，便于调试或验证
    return {
        "n": n,
        "k": k,
        "a": a,
        "result": result
    }

if __name__ == "__main__":
    # 示例：调用 main(10)
    output = main(10)
    print(output["result"])