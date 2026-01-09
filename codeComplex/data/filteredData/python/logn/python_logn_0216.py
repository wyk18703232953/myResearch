import sys
import math
import queue
import bisect

MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

def ok(x, s):
    y = sum(map(int, list(str(x))))
    return x - y >= s

def main(n):
    """
    n: 问题规模，用于生成测试数据
    测试数据生成规则（可根据需要调整）：
      - 令 s = n // 2
      - 搜索区间为 [0, n]
    输出与原程序一致的结果：满足 x - sum_digits(x) >= s 的 x 的个数
    """
    # 生成测试数据
    s = n // 2

    l, h = 0, n
    a = n
    while l <= h:
        m = (l + h) >> 1
        if ok(m, s):
            a = m - 1
            h = m - 1

        else:
            l = m + 1
    result = n - a
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例调用：可修改 n 以测试不同规模
    main(10**6)