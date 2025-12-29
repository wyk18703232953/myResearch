def get_max(n):
    ans = 0
    while n:
        ans = 4 * ans + 1
        n -= 1
        if ans > 10**19:
            break
    return ans


def solve_case(n, k):
    if n == 1:
        if k == 1:
            return "YES 0"
        else:
            return "NO"
    elif n == 2:
        if k <= 2:
            return "YES 1"
        elif k != 3 and k <= 5:
            return "YES 0"
        else:
            return "NO"
    else:
        siz = n - 1
        l = 1
        cnt = 3
        while siz:
            if l <= k < l + cnt:
                return f"YES {siz}"
            l = l + cnt
            cnt = 2 * cnt + 1
            siz -= 1
        else:
            if k <= get_max(n):
                return "YES 0"
            else:
                return "NO"


def main(n):
    # 根据规模 n 生成测试数据：
    # 使用 n 作为测试组数 t，每组的 (n_i, k_i) 也由 n 派生。
    # 这里只是一个示例生成方式，可按需要修改：
    t = n
    results = []
    for i in range(1, t + 1):
        # 生成 n_i 和 k_i
        ni = i % 10 + 1      # n_i 在 1~10 之间
        # k_i 尝试覆盖不同大小区间
        ki = i * 2 + 1
        results.append(solve_case(ni, ki))

    # 输出所有结果
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)