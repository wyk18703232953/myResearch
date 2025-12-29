from collections import defaultdict
import random

def main(n):
    # 生成测试数据：随机选择 k，随机生成长度为 n 的数组 arr
    # 这里假设数值规模在 [0, 2^k - 1] 范围内
    if n <= 0:
        print(0)
        return

    # 选择一个合适的 k，使得 2^k 不太小也不太大
    # 例如 k 在 [1, 20] 中随机选一个
    k = random.randint(1, 20)

    arr = [random.randint(0, (1 << k) - 1) for _ in range(n)]

    xors = defaultdict(int)
    xors[0] = 1
    comp = (1 << k) - 1
    xor_val = 0
    ans = n * (n + 1) // 2

    for a in arr:
        xor_val ^= a
        if xors[xor_val] > xors[comp ^ xor_val]:
            xor_val ^= comp
        ans -= xors[xor_val]
        xors[xor_val] += 1

    print(ans)

if __name__ == "__main__":
    # 示例调用，规模 n 可按需修改
    main(10)