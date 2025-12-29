from collections import defaultdict
import random

def solve_one_case(a):
    n = len(a)
    dd = defaultdict(int)
    for i in range(n):
        dd[a[i]] += 1

    l = []
    for aa in a:
        if dd[aa] >= 2:
            l.append(aa)
            dd[aa] -= 2

    l.sort()
    ans = [-1, -1, -1, -1]
    m = 10**18
    for i in range(len(l) - 1):
        x = (4 * (l[i] + l[i + 1]) ** 2) / (l[i] * l[i + 1])
        if x < m:
            ans = [l[i], l[i], l[i + 1], l[i + 1]]
            m = x
    return ans

def main(n):
    """
    n: 规模参数，用于生成测试数据。
       这里生成 t 个测试用例，每个用例长度约为 n。
    """
    random.seed(0)

    # 生成测试用例个数，可以根据需要调整，这里简单设为 3
    t = 3

    for _ in range(t):
        # 生成一个长度在 [max(4, n//2), n] 之间的数组
        length = max(4, random.randint(max(4, n // 2), max(4, n)))
        # 为了增加可用的成对元素，生成元素在 1..(n//2+1) 范围内
        a = [random.randint(1, max(2, n // 2 + 1)) for _ in range(length)]
        ans = solve_one_case(a)
        print(*ans)

if __name__ == "__main__":
    # 示例：以 n=10 运行
    main(10)