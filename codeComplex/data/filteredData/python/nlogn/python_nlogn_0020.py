import random

def main(n: int):
    # 生成规模为 n 的测试数据：n 个随机整数，范围可根据需要调整
    # 为了尽量模拟原题含义，这里允许重复与负数
    data = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原始逻辑：从输入序列中找第二小的不同数
    a = sorted(set(data))

    if len(a) > 1:
        x = iter(a)
        next(x)   # 跳过最小的
        print(next(x))  # 打印第二小的不同元素
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)