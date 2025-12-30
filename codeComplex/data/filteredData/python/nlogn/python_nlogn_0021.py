import random

def main(n):
    # 1. 生成测试数据：n 个随机整数
    # 为了体现原程序逻辑，允许重复元素
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原逻辑封装
    a_set = set(a)
    a_sorted = sorted(a_set)

    if len(a_sorted) == 1:
        print("NO")
    else:
        print(a_sorted[1])


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)