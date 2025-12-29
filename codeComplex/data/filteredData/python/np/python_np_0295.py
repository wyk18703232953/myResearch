import math
import collections
import random

MOD = 10**9 + 7

def solve(nums):
    count = collections.defaultdict(int)
    for num in nums:
        for i in range(1, int(math.isqrt(num)) + 1):
            if num % i == 0:
                cp = num // i
                count[i] += 1
                if cp != i:
                    count[cp] += 1

    if not count:
        return 0

    maxk = max(count.keys())
    freq = {k: (1 << count[k]) - 1 for k in count}

    for k in sorted(count.keys(), reverse=True):
        mul = k << 1
        while mul <= maxk:
            if mul in freq:
                freq[k] -= freq[mul]
            mul += k

    return freq.get(1, 0) % MOD

def main(n):
    # 生成规模为 n 的测试数据：n 个正整数
    # 这里生成 1 到 10^6 之间的随机数，可根据需要调整
    random.seed(0)
    nums = [random.randint(1, 10**6) for _ in range(n)]
    ans = solve(nums)
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模设为 10
    main(10)