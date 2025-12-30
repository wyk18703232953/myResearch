from collections import Counter
import copy
import random

def solve(a, b):
    count = 0
    if a == b:
        return 1
    while a != 0 and b != 0:
        if a < b:
            count += (b // a)
            b -= a * (b // a)
        else:
            count += a // b
            a -= b * (a // b)
    return count

def main(n):
    """
    n: 测试数据规模，表示生成 n 组 (a, b) 测试数据并依次求解。
    测试数据生成规则：a, b 为 [1, 10^6] 之间的随机正整数。
    """
    random.seed(0)
    results = []
    for _ in range(n):
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        results.append(solve(a, b))
    return results

if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    output = main(5)
    for ans in output:
        print(ans)