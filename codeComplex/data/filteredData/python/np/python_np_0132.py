import random
import math

def main(n):
    # 生成规模为 n 的测试数据
    # 这里假设原代码中两行输入长度相同，长度为 n
    # 生成 1..10^9 范围内的随机整数
    ps = [random.randint(1, 10**9) for _ in range(n)]
    cs = [random.randint(1, 10**9) for _ in range(n)]

    acc = {0: 0}
    for p, c in zip(ps, cs):
        adds = []
        # 根据原代码逻辑计算 gcd，并更新代价
        for b, u in acc.items():
            a = p
            bb = b
            # 这里使用和原代码等价的求 gcd 方式
            while bb:
                a, bb = bb, a % bb
            adds.append((a, u + c))
        for a, u in adds:
            acc[a] = min(u, acc.get(a, 10**9))

    ans = acc.get(1, -1)
    print(ans)
    return ans

if __name__ == '__main__':
    # 示例：调用 main(5)，规模为 5
    main(5)