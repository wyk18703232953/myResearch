from collections import defaultdict
import random

def solve(arr, k):
    n = len(arr)
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
    return ans

def main(n):
    # 根据 n 生成测试数据：
    # 让 k = min(20, max(1, n.bit_length()))，数组元素在 [0, 2^k-1] 之间随机生成
    if n <= 0:
        return 0
    k = min(20, max(1, n.bit_length()))
    max_val = (1 << k) - 1
    random.seed(0)
    arr = [random.randint(0, max_val) for _ in range(n)]
    ans = solve(arr, k)
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模 n，可自行修改
    main(5)