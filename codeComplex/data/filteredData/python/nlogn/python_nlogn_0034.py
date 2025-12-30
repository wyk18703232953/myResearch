import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据，这里生成 n 个 1~10^9 范围内的随机整数
    lst = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原始逻辑
    lst = list(set(lst))          # 去重
    if not lst:
        print("NO")
        return

    lst.remove(min(lst))          # 删除最小值
    if len(lst) == 0:
        print("NO")
    else:
        print(min(lst))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)