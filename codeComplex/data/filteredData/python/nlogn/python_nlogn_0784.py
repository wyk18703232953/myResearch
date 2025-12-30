import random

def main(n):
    # 生成测试数据
    # 随机生成 k，1 <= k <= n
    k = random.randint(1, n)
    # 生成一个递增数组 A，模拟原题中常见的情形
    # 先生成随机起点
    start = random.randint(0, 10)
    A = [start]
    for _ in range(1, n):
        # 每一步增加 0~10 的随机差值
        A.append(A[-1] + random.randint(0, 10))

    # 原逻辑开始
    B = []
    for i in range(1, n):
        B.append(A[i] - A[i - 1])
    B.sort()
    result = sum(B[:n - k])

    # 输出结果（可按需改为 return result）
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)