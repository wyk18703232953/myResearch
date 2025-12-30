import random

def main(n: int):
    # 根据 n 生成测试数据
    # 保证 a, b, c, n 为正整数，且不超过 n
    a = random.randint(1, n)
    b = random.randint(1, n)
    c = random.randint(1, n)
    # 也可以让 n 做为「总量」，此处示例中保持传入的 n 不变
    # 若需要可改为：total = random.randint(max(a, b, c), n)

    # 将原始逻辑封装
    if (c > b or c > a or c > n):
        print(-1)
    else:
        k = c + (a - c) + (b - c)
        k = n - k
        if k > 0:
            print(k)
        else:
            print(-1)

if __name__ == "__main__":
    # 示例：调用 main(100) 作为规模为 100 的测试
    main(100)