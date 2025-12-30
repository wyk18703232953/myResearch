def sum_range(x: int) -> int:
    return (x * (x + 1)) // 2


def bs(st: int, en: int, n: int, k: int, s: int) -> int:
    while st < en:
        mid = st + (en - st) // 2
        s1 = s - sum_range(mid - 1)

        if s1 == n:
            return (k - mid) + 1
        elif s1 > n:
            st = mid + 1
        else:
            en = mid
    return (k - st) + 2


def main(n: int):
    """
    n 作为规模参数，用于生成测试数据。
    这里简单设定：
        原程序中有效的是 n-1 和 k-1 以及 sum_range(k-1) 与 n-1 的关系。
    为了能覆盖各种分支，给出一个较自然的构造方式：
        - 取 k = n // 2 + 1 （保证 k 不太小）
    你可以根据需要自行调整生成规则。
    """
    # 生成测试数据 (N, K)
    N = max(1, n)         # 保证 N >= 1
    K = max(1, n // 2 + 1)

    # 对应原始代码的变量变换
    n_val = N - 1
    k_val = K - 1
    s_val = sum_range(k_val)

    # 对应原始逻辑的输出
    if n_val + 1 == 1:
        print(0)
    elif n_val <= k_val:
        print(1)
    elif n_val > s_val:
        print(-1)
    else:
        print(bs(1, k_val, n_val, k_val, s_val))


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)