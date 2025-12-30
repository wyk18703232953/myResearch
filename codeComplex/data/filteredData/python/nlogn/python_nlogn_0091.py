import random

def main(n):
    # 随机生成 a, b，满足 1 <= a <= n，1 <= b < n
    a = random.randint(1, n)
    b = random.randint(1, n - 1)

    # 根据 n 生成 n 个随机整数作为测试数据
    # 这里生成范围可根据需要调整
    l = [random.randint(0, 10**9) for _ in range(n)]

    # 按原逻辑处理
    l.sort()
    result = l[b] - l[b - 1]
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模可按需修改
    main(10)