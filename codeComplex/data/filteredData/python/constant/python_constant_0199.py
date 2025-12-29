import random

def main(n):
    # 生成规模为 n 的测试数据：n 个 1~5 之间的随机整数
    l = [random.randint(1, 5) for _ in range(n)]
    l = sorted(l)

    # 为保持与原逻辑一致，只在 n >= 3 时安全访问下标 0,1,2
    cond = False
    if l and min(l) == 1:
        cond = True
    elif n >= 3:
        if (l[0] == 3 and l[1] == 3 and l[2] == 3) or \
           (l[0] == 2 and l[1] == 4 and l[2] == 4) or \
           (l[0] == 2 and l[1] == 2):
            cond = True

    print("Yes" if cond else "No")


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)