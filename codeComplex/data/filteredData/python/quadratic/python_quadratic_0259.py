from collections import defaultdict
import random

def main(n: int) -> None:
    """
    使用规模 n 自动生成 a, b，并运行原程序的逻辑。
    输出与原程序相同的图的邻接矩阵或 NO。
    """
    # 1. 根据 n 生成测试数据 (a, b)
    #    保持在 [1, n] 范围内
    if n < 2:
        # 原题本身对很小 n 没有意义，这里直接输出 NO
        print("NO")
        return

    a = random.randint(1, n)
    b = random.randint(1, n)

    # ---- 以下是原程序逻辑，去掉 input() 并封装 ----

    hash_map = defaultdict(list)  # 保留原变量名 hash 的语义，避免覆盖内置 hash

    if a == 1 and b == 1:
        if n == 2 or n == 3:
            print("NO")
            return

    if a == 1 or b == 1:
        used = [False] * (n + 1)

        if a > n or b > n:
            print("NO")
            return

        print("YES")

        # 初始化矩阵 l
        l = []
        for _ in range(n):
            z = ["0"] * n
            l.append(z)

        # 初始化矩阵 ans
        ans = []
        for _ in range(n):
            z = ["0"] * n
            ans.append(z)

        if b == 1:
            # 构造链
            for i in range(a - 1, n - 1):
                l[i][i + 1] = "1"
                l[i + 1][i] = "1"

            for row in l:
                print("".join(row))
        else:
            # 重新初始化 ans（保持与原代码一致）
            ans = []
            for _ in range(n):
                z = ["0"] * n
                ans.append(z)

            # 构造链
            for i in range(b - 1, n - 1):
                l[i][i + 1] = "1"
                l[i + 1][i] = "1"

            # 取反生成 ans
            for i in range(n):
                for j in range(n):
                    if i != j:
                        if l[i][j] == "1":
                            ans[i][j] = "0"
                        elif l[i][j] == "0":
                            ans[i][j] = "1"

            for row in ans:
                print("".join(row))

    else:
        print("NO")