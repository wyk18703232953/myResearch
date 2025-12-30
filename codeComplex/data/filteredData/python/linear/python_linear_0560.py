from collections import defaultdict
import random

def main(n):
    # 生成测试数据：
    # 这里我们选择一个固定的 k（例如 20），并生成 n 个在 [0, 2^k-1] 范围内的随机整数
    k = 20
    max_val = (1 << k) - 1
    arr = [random.randint(0, max_val) for _ in range(n)]

    # 原逻辑开始
    xors = defaultdict(int)
    xors[0] = 1
    comp = (1 << k) - 1
    ans = n * (n + 1) // 2
    xor = 0

    for a in arr:
        xor ^= a
        if xors[xor] > xors[comp ^ xor]:
            xor ^= comp
        ans -= xors[xor]
        xors[xor] += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 可按需调整
    main(10)