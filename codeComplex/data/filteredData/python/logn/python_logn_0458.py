import random

mod = 10 ** 9 + 7

# 模拟交互：隐藏的 A, B
_hidden_A = 0
_hidden_B = 0


def ask(x, y):
    """
    原题里的交互函数：
    返回：
    1  若 (A ^ x) > (B ^ y)
    -1 若 (A ^ x) < (B ^ y)
    0  若 (A ^ x) == (B ^ y)
    这里用隐藏的 _hidden_A, _hidden_B 来模拟。
    """
    ax = _hidden_A ^ x
    by = _hidden_B ^ y
    if ax > by:
        return 1
    elif ax < by:
        return -1
    else:
        return 0


def main(n: int):
    """
    n 为规模，用于生成测试数据：
    - 取 A, B 在 [0, 2^n - 1] 中随机
    - 使用原算法推回 A, B
    - 返回 (真实 A, 真实 B, 推断的 A, 推断的 B)
    """
    global _hidden_A, _hidden_B

    if n <= 0:
        n = 1
    if n > 30:
        n = 30  # 原程序最多用了 0..29 共 30 位

    upper = 1 << n
    _hidden_A = random.randrange(upper)
    _hidden_B = random.randrange(upper)

    # ---- 原始逻辑开始 ----
    a = 0
    b = 0
    cond = ask(a, b)
    for i in range(29, -1, -1):
        if cond:
            x = a + (1 << i)
            y = b + (1 << i)
            n_cond = ask(x, y)
            if cond == n_cond:
                if cond == 1:
                    n_cond1 = ask(x, b)
                else:
                    n_cond1 = ask(a, y)

                if cond != n_cond1:
                    a = x
                    b = y

            else:
                if cond == 1:
                    a = x
                else:
                    b = y
                cond = ask(a, b)
        else:
            x = a + (1 << i)
            y = b + (1 << i)
            n_cond = ask(x, b)
            if n_cond == -1:
                a = x
                b = y
    # ---- 原始逻辑结束 ----

    # 为了便于自动测试，这里返回结果
    return _hidden_A, _hidden_B, a, b


if __name__ == "__main__":
    # 示例：运行 5 次测试
    for n in [5, 10, 15, 20, 30]:
        A, B, a, b = main(n)
        print(f"n={n}, real=({A}, {B}), found=({a}, {b}), ok={A == a and B == b}")