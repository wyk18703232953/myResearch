import math
import random

def main(n):
    # 生成测试数据：
    # n：规模（给定）
    # m：1 ~ n
    # k：0 ~ n
    # l：0 ~ n
    if n <= 0:
        return
    m = random.randint(1, n)
    k = random.randint(0, n)
    l = random.randint(0, n)

    # 原逻辑开始
    ost = n - k
    need = (l + k)
    if ost < l or need > n:
        print(-1)
        return
    ans = (l + k - 1) // m + 1
    if ans * m - k >= l and ans * m <= n:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)