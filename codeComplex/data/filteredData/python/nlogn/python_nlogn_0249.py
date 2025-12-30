from bisect import bisect_right
import random

def main(n):
    # 生成测试数据
    # a 为长度 n 的正整数数组
    a = [random.randint(1, 10) for _ in range(n)]
    # q 的规模可与 n 相同，这里设为 n
    q = n
    # k 为长度 q 的正整数数组
    k = [random.randint(1, 10) for _ in range(q)]

    # 原逻辑开始
    for i in range(1, n):
        a[i] += a[i - 1]

    an = 0
    for j in k:
        j += an
        x = bisect_right(a, j)
        if x == n:
            print(n)
            an = 0
        else:
            print(n - x)
            an = j

if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)