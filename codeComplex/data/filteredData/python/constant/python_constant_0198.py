import random

def main(n):
    # 生成规模为 n 的测试数据：n 个 1~10 的随机整数
    l = [random.randint(1, 10) for _ in range(n)]
    l.sort()

    # 只在 n >= 3 时，才与原逻辑完全一致
    if n >= 3 and (
        min(l) == 1 or
        (l[0] == 3 and l[1] == 3 and l[2] == 3) or
        (l[0] == 2 and l[1] == 4 and l[2] == 4) or
        (l[0] == 2 and l[1] == 2)
    ):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)