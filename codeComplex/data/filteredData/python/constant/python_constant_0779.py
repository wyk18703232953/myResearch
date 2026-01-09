def solve(N):
    if N % 2 != 0:
        return "NO"
    N //= 2
    if int(N ** 0.5) ** 2 == N:
        return "YES"
    if N % 2 != 0:
        return "NO"
    N //= 2
    if int(N ** 0.5) ** 2 == N:
        return "YES"
    return "NO"


def main(n):
    """
    n 为测试规模，这里生成 n 个测试样例并依次调用 solve。
    测试数据策略（可按需要修改）：
    - 第 i 个样例 N = i
    """
    for i in range(1, n + 1):
        N = i  # 生成第 i 个测试数据
        ans = solve(N)
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：运行 main(10) 做简单测试
    main(10)