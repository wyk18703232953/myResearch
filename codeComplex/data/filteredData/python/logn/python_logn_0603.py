import sys
sys.setrecursionlimit(100000)

def main(n):
    # 生成规模为 n 的测试数据：
    # 这里构造 k 为 estimate(x) 的某个值，保证有解
    # 选取 x = n // 2 作为目标
    x = n // 2

    def estimate(a):
        return int(((n - a) * (n + 1 - a)) / 2) - a

    k = estimate(x)  # 生成对应的 target

    def dicho(lower, upper, target):
        if estimate(lower) == target:
            return lower
        elif estimate(upper) == target:
            return upper

        else:
            mid = (lower + upper) // 2
            if estimate(mid) < target:
                upper = mid

            else:
                lower = mid
            return dicho(lower, upper, target)

    lower = 0
    upper = n
    ans = dicho(lower, upper, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可修改这里的 n 来运行不同规模
    main(10)