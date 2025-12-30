from collections import Counter
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # p: 目标数量，随机取 1..n
    # 然后生成 n 个在 1..n 之间的整数作为多重集
    p = random.randint(1, n)
    arr = [random.randint(1, n) for _ in range(n)]
    d = Counter(arr)

    def pos(x):
        # 判断是否可以从多重集 d 中组成至少 p 个组，
        # 每组大小为 x（允许不同数字混用，但本题原意是按数字独立算）。
        # 原程序逻辑是：对每个数的频次 v，能贡献 v // x 个完整组，
        # 然后检查所有贡献之和是否 >= p
        t = 0
        for v in d.values():
            if v >= x:
                t += v // x
        return t >= p

    ans = 0
    for sel in range(1, n + 1):
        if pos(sel):
            ans = max(ans, sel)

    # 输出结果（也可以 return ans 看使用场景）
    print("n =", n)
    print("p =", p)
    print("array =", arr)
    print("max group size =", ans)
    return ans

if __name__ == "__main__":
    # 示例运行：可以改为任意规模
    main(10)