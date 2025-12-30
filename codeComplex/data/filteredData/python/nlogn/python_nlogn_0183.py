from collections import Counter
import random

def d(ar):
    n = len(ar)
    me = Counter()
    s = 0
    for i in range(n):
        s += i * ar[i]
        s -= (me[ar[i]] + me[ar[i] + 1] * ar[i] + me[ar[i] - 1] * ar[i])
        me[ar[i]] += 1
    return s

def main(n):
    # 生成测试数据：长度为 n 的整数数组
    # 这里示例为在区间 [0, n] 上均匀随机
    ar = [random.randint(0, n) for _ in range(n)]
    rev = ar[::-1]
    result = d(ar) - d(rev)
    print(result)

if __name__ == "__main__":
    # 示例运行：可修改 n 测试不同规模
    main(10)