import random

def main(n):
    # 根据 n 生成测试数据 (a, b)
    # 这里给出一种生成策略：随机生成 1~n 之间的 a, b，然后强制满足题目中的合法性条件之一。
    if n <= 1:
        # 原题逻辑在 n=1 情况下没有特别说明，这里给出一个简单退化情况
        a, b = 1, 1
    else:
        # 随机选择一种合法模式进行测试：
        # 1) a>1, b=1 且不触发 (n==2或3且a==1且b==1)
        # 2) a=1, b>1
        # 3) a=1, b=1 且 n 不在 {2,3}
        mode = random.choice([1, 2, 3])
        if mode == 1:
            # a>1, b=1
            a = random.randint(2, n)
            b = 1
            if (n in (2, 3)) and (a == 1 and b == 1):  # 实际不会触发，只是保持结构一致
                a = 2
        elif mode == 2:
            # a=1, b>1
            a = 1
            b = random.randint(2, n)
        else:
            # a=1, b=1 且 n 不在 {2,3}
            a, b = 1, 1
            if n in (2, 3):
                # 如果 n 太小，为避免 "NO" 分支，退回到 a>1, b=1
                a = 2
                b = 1

    # 下面是原始逻辑（去掉 input/exit，改为在函数内返回/打印）
    if (n == 3 or n == 2) and (a == 1 and b == 1):
        print("NO")
        return

    g = [[0 for _ in range(n)] for _ in range(n)]

    if a > 1 and b == 1:
        for i in range(n - a - 1, -1, -1):
            g[i][i + 1] = g[i + 1][i] = 1
    elif b > 1 and a == 1:
        a, b = b, a
        for i in range(n - a - 1, -1, -1):
            g[i][i + 1] = g[i + 1][i] = 1
        for i in range(n):
            for j in range(n):
                if g[i][j] == 0:
                    g[i][j] = 1
                elif g[i][j] == 1:
                    g[i][j] = 0
        for i in range(n):
            g[i][i] = 0
    elif a == 1 and b == 1:
        for i in range(n - 1):
            g[i][i + 1] = g[i + 1][i] = 1
    elif a > 1 and b > 1:
        print("NO")
        return

    print("YES")
    for i in range(n):
        for j in range(n):
            print(g[i][j], end='')
        print()


# 示例：直接调用 main(5) 进行一次测试
if __name__ == "__main__":
    main(5)