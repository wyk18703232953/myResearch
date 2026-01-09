# B. Preparing Olympiad - parameterized version

def main(n):
    """
    n: problem count / scale
    自动生成测试数据：
      - l = 10, r = 1000, x = 10
      - c 为 1..n 的整数难度
    返回：满足条件的组合数量
    """
    # 生成测试数据
    global l, r, x, problems, combination, ans

    l = 10
    r = 1000
    x = 10
    c = list(range(1, n + 1))  # 示例难度：1, 2, ..., n

    def check_combination(v):
        sm = sum(v)
        if l <= sm <= r:
            if max(v) - min(v) >= x:
                nonlocal ans
                ans += 1

    def go(offset, k):
        # 生成所有大小为 k 的组合
        if k == 0:
            check_combination(combination)
            return
        for i in range(offset, len(problems) - k + 1):
            combination.append(problems[i])
            go(i + 1, k - 1)
            combination.pop()

    problems = []
    combination = []
    ans = 0

    for i in range(2, len(c) + 1):
        problems = c.copy()
        go(0, i)

    return ans


# 示例运行
if __name__ == "__main__":
    # 可修改 n 进行不同规模测试
    result = main(10)
    # print(result)
    pass