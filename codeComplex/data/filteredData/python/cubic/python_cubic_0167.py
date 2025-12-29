import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 这里生成 1..n 的随机整数，可按需要自定义分布
    random.seed(0)
    a = [random.randint(1, n) for _ in range(n)]

    grip = [[-1] * (n - i) for i in range(n)]
    grip[0] = a.copy()

    for level in range(1, n):
        for left in range(n - level):
            for split in range(level):
                pl = grip[level - split - 1][left]
                pr = grip[split][left + level - split]
                if pl == pr != -1:
                    grip[level][left] = pl + 1

    pref = [0] * (n + 1)
    for p in range(1, n + 1):
        x = n
        for j in range(p):
            l = pref[j]
            r = grip[p - j - 1][j]
            if r == -1:
                r = p - j
            else:
                r = 1
            x = min(x, l + r)
        pref[p] = x

    # 保持原程序行为：输出最终答案
    print(pref[-1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)