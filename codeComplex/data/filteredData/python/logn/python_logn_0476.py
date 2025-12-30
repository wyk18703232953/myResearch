from random import randint

# 目标：将交互式程序改为可本地测试的程序
# main(n) 中：
#   1. 生成规模为 n 的测试数据 a, b（这里用 n 控制比特位数）
#   2. 使用 get_ans 模拟交互，运行原算法逻辑
#   3. 返回 (a, b, curaM, curbM)，其中 curaM, curbM 是算法求出的值


def get_ans(a, b, c, d, curaM, curbM):
    """
    模拟原交互：返回 (a^c^curaM) 与 (b^d^curbM) 的大小关系：
    1  : a_ > b_
    -1 : a_ < b_
    0  : a_ == b_
    """
    a_ = a ^ c ^ curaM
    b_ = b ^ d ^ curbM

    if a_ > b_:
        return 1
    if a_ < b_:
        return -1
    return 0


def solve_for_a_b(a, b, max_bit=29):
    """
    将原交互逻辑改写为调用 get_ans 的函数。
    给定隐藏数 a, b，返回推断出的 (curaM, curbM)。
    max_bit 控制最高位（原代码固定 29）。
    """
    curaM = 0
    curbM = 0
    curC = get_ans(a, b, 0, 0, 0, 0)

    for i in range(max_bit, -1, -1):
        ans1 = get_ans(a, b, 1 << i, 0, curaM, curbM)
        ans2 = get_ans(a, b, 0, 1 << i, curaM, curbM)

        if ans1 * ans2 >= 0:
            if curC == 1:
                curaM |= 1 << i
            elif curC == -1:
                curbM |= 1 << i
            curC = ans1
        else:
            if ans1 < 0:
                curaM |= 1 << i
                curbM |= 1 << i

    return curaM, curbM


def main(n):
    """
    n 为规模参数：
    - 使用 n 位来生成随机 a, b：0 <= a, b < 2^n
    - 运行算法，返回 (a, b, curaM, curbM)

    你可以根据需要调整 n 与 max_bit 的关系：
    - 若 n <= 30，默认 max_bit = n-1
    - 若 n > 30，仍然只用 0..29 位（保持和原程序一致）
    """
    if n <= 0:
        # 处理无意义规模
        return 0, 0, 0, 0

    # 控制最高位，保持与原代码兼容（最大 29）
    max_bit = min(29, n - 1)
    limit = 1 << (max_bit + 1)

    # 生成测试数据 a, b
    a = randint(0, limit - 1)
    b = randint(0, limit - 1)

    curaM, curbM = solve_for_a_b(a, b, max_bit=max_bit)

    # 原交互程序最终输出的是 curaM, curbM
    # 这里返回原始 a, b 和结果，方便测试
    return a, b, curaM, curbM


if __name__ == "__main__":
    # 示例：规模 n = 30
    n = 30
    a, b, x, y = main(n)
    print("a =", a, "b =", b)
    print("curaM =", x, "curbM =", y)