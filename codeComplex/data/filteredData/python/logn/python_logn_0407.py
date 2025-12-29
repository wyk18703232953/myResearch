def get_max(n):
    ans = 0
    while n:
        ans = 4 * ans + 1
        n = n - 1
        if ans > 10**19:
            break
    return ans


def solve_one(n, k):
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
            siz = siz - 1
        else:
            if k <= get_max(n):
                return "YES 0"
            else:
                return "NO"


def main(t):
    """
    t: 测试规模（用作测试数据中 n 的最大值，同时生成 t 组数据）
    根据 n 规模自动生成 t 组 (n, k) 测试数据并输出对应结果。
    这里的 n 在 [1, t] 内变化，k 在 [1, get_max(n)] 范围内截断。
    """
    results = []
    for i in range(1, t + 1):
        n = i
        # 生成一个覆盖性的 k，简单取 get_max(n)//2 + 1（并截断到至少 1）
        k_candidate = get_max(n) // 2 + 1
        if k_candidate <= 0:
            k_candidate = 1
        k = k_candidate
        res = solve_one(n, k)
        results.append(res)
        print(res)
    return results


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)