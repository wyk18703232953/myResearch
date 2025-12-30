import random

class Solution2:
    def solve(self, s):
        pass


class Solution:
    def solve(self, n, k):
        grow = 1
        tot = 0

        while n != tot - k:
            tot += grow
            grow += 1
            n -= 1
        return tot - k


sol = Solution()
sol2 = Solution2()


def main(n):
    """
    n 为规模参数，用来生成一组 (N, K) 测试数据并运行原逻辑。
    这里简单设定：
      N = n
      K 在 [0, n//2] 范围内随机生成
    """
    if n <= 0:
        return

    N = n
    K = random.randint(0, max(0, n // 2))

    out = sol.solve(N, K)
    print(str(out))


if __name__ == "__main__":
    # 示例：用某个规模调用 main
    main(10)