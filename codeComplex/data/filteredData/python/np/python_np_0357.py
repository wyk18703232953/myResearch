rnd_mod = 1234567890133
rnd_x = 987654321098

def rnd():
    global rnd_x
    rnd_x = rnd_x**2 % rnd_mod
    return (rnd_x >> 5) % (1 << 20)

def randrange(a):
    return rnd() % a

def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里将 N = n, M = max(1, n//2)。
    返回：运行一次测试用例得到的结果 ma。
    """
    global rnd_x
    rnd_x = 987654321098  # 重置随机数种子，保证可复现

    T = 1  # 生成 1 组测试数据
    results = []

    for _ in range(T):
        N = n
        M = max(1, n // 2)

        # 生成测试数据 X：N 行，每行 M 个非负整数
        # 数值范围与原 rnd 函数输出一致：0 <= val < 2^20
        X = [[rnd() for _ in range(M)] for __ in range(N)]

        # 转置矩阵：Y 是 M 行 N 列
        Y = [[X[i][j] for i in range(N)] for j in range(M)]

        ma = 0
        for _t in range(577):
            # 对每一列（在 Y 中是每一行 i）做循环平移
            for i in range(M):
                a = randrange(N)
                Y[i] = [Y[i][(j - a) % N] for j in range(N)]
            # 按列取最大值并求和
            ma = max(ma, sum(max(Y[i][j] for i in range(M)) for j in range(N)))

        results.append(ma)

    # 原代码是直接 print，这里 main 返回结果
    # 若需要完全一致的行为，可在这里打印：
    # for r in results:
    #     print(r)
    return results[0] if T == 1 else results

if __name__ == "__main__":
    # 示例：规模为 10
    print(main(10))