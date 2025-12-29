from itertools import accumulate
import random

def main(n):
    # 生成测试数据：
    # n: 数组长度
    # k: 随机选择一个 >=2 的整数
    # a: 长度为 n 的随机整数数组
    random.seed(0)
    k = random.randint(2, 10)
    a = [random.randint(1, 100) for _ in range(n)]

    # 原始逻辑开始
    a.sort()
    s = set()
    for v in a:
        if (v % k != 0) or v // k not in s:
            s.add(v)
    print(len(s))

if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)