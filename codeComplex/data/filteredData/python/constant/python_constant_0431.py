import random

def main(n):
    # 生成测试数据：k 在 [1, 2n+2] 范围内随机取值，确保覆盖边界情况
    # 也可以根据需要改为其他生成方式
    k = random.randint(1, 2 * n + 2)

    # 原始逻辑
    if k > n * 2 or k < 3:
        print(0)
    elif n >= k - 1:
        print(k - k // 2 - 1)
    else:
        print(n - k // 2)


if __name__ == "__main__":
    # 示例：调用 main，n 可在此处修改或由外部调用 main(n)
    main(10)