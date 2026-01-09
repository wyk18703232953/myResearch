def checksq(n):
    m = int(n**0.5)
    if m * m == n:
        return m
    m += 1
    if m * m == n:
        return m
    return -1

def solve_single(n):
    if n % 2 == 1:
        return "NO"
    if checksq(n // 2) != -1:
        return "YES"
    n //= 2
    if n % 2 == 1:
        return "NO"
    if checksq(n // 2) != -1:
        return "YES"

    else:
        return "NO"

def main(n):
    # 解释规模含义：
    # n 表示测试用例数量 T
    # 第 i 个用例的输入值为 i（从 1 到 n）
    results = []
    for i in range(1, n + 1):
        results.append(solve_single(i))
    # 为了避免大量 I/O 对时间的干扰，仅在最后统一输出
    # print("\n".join(results))
    pass
if __name__ == "__main__":
    # 示例：以 10 作为规模参数运行
    main(10)