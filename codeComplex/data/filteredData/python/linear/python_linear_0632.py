def A(n):
    return (4 ** n - 1) // 3

L = 31

def run_single_case(n, k):
    if n > L:
        return "YES " + str(n - 1)

    if k > A(n):
        return "NO"

    E = 1
    M = 0
    R = 0
    nn = n
    while nn >= 0:
        M += E

        I = 2 * E - 1
        E = 2 * E + 1

        nn -= 1
        R += I * A(nn)

        if M <= k <= M + R:
            break

    if nn >= 0:
        return "YES " + str(nn)
    else:
        return "NO"

def main(n):
    # 将 n 视作测试用例数量规模
    T = n if n > 0 else 1
    results = []

    for i in range(1, T + 1):
        # 确定性生成每组 (n_i, k_i)
        n_i = 1 + (i % 40)  # 保持在相对小的范围内，且含有 n > L 的情况
        k_i = (i * i + 3 * i) // 2  # 简单确定性算式生成 k

        res = run_single_case(n_i, k_i)
        results.append(res)

    for r in results:
        print(r)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模调用
    main(10)