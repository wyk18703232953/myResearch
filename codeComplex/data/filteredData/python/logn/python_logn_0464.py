import random

def judge(x, y, A, B):
    """模拟交互：比较 x^2 + A 与 y^2 + B 的大小。
       返回值规则与原题交互相同：
       返回 0  表示 x^2 + A == y^2 + B
       返回 1  表示 x^2 + A  > y^2 + B
       返回 -1 表示 x^2 + A  < y^2 + B
    """
    v1 = x * x + A
    v2 = y * y + B
    if v1 == v2:
        return 0
    return 1 if v1 > v2 else -1


def solve(keta, A, B):
    """
    将原交互式逻辑改写成直接调用 judge 的离线版本，
    返回推断出的 (A_ans, B_ans)。
    """
    # 对应原代码中第一次查询: "?", 0, 0
    A00 = judge(0, 0, A, B)

    if A00 == 0:
        ANS = 0
        # 原代码: for k in range(keta, -1, -1)
        for k in range(keta, -1, -1):
            # 对应查询: "?", 2**k, 0
            res = judge(2 ** k, 0, A, B)
            if res == -1:
                ANS += 2 ** k
        # 原代码输出: "!", ANS, ANS
        return ANS, ANS

    A_ans = 0
    B_ans = 0
    for k in range(keta, -1, -1):
        # 对应查询: "?", 2**k + A, B
        res1 = judge(2 ** k + A_ans, B_ans, A, B)
        # 对应查询: "?", A, 2**k + B
        res2 = judge(A_ans, 2 ** k + B_ans, A, B)

        if res1 != res2:
            if res1 == -1:
                A_ans += 2 ** k
                B_ans += 2 ** k
        else:
            if A00 == 1:
                A_ans += 2 ** k
            else:
                B_ans += 2 ** k
            A00 = res1

    return A_ans, B_ans


def main(n):
    """
    n 为规模参数，用来控制随机生成 A,B 的范围和使用的二进制位数 keta。
    这里的设定为:
      - 生成 0 <= A,B < 2^n
      - keta = n-1 (最高位索引)
    返回 (真实A, 真实B, 推断A, 推断B) 便于测试验证。
    """
    if n <= 0:
        raise ValueError("n 必须为正整数")

    # 根据 n 设置位数和随机范围
    keta = n - 1
    max_val = 1 << n  # 2^n

    # 生成测试数据 A, B
    A = random.randrange(0, max_val)
    B = random.randrange(0, max_val)

    # 运行算法
    A_ans, B_ans = solve(keta, A, B)

    # 仅作为示例返回值，真实使用时可根据需要改为 print 或其他形式
    return A, B, A_ans, B_ans


if __name__ == "__main__":
    # 示例：用 n = 29 运行一次测试
    A_real, B_real, A_found, B_found = main(29)
    print("Real A,B   :", A_real, B_real)
    print("Found A,B  :", A_found, B_found)