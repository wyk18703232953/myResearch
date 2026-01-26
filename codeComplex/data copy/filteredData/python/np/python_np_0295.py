import math
import collections

MOD = 10**9 + 7

def core(nums):
    count = collections.defaultdict(int)
    for num in nums:
        for i in range(1, int(math.isqrt(num)) + 1):
            cp = num // i
            if num % i == 0:
                count[i] += 1
            if cp != i and num % cp == 0:
                count[cp] += 1
    if not count:
        return 0
    maxk = max(count.keys())
    freq = {k: (1 << count[k]) - 1 for k in count}
    for k in sorted(count.keys(), reverse=True):
        for kk in range(k << 1, maxk + 1, k):
            if kk in freq:
                freq[k] -= freq[kk]
    return freq.get(1, 0) % MOD

def main(n):
    if n <= 0:
        return 0
    nums = [i + 1 for i in range(n)]
    return core(nums)

if __name__ == "__main__":
    print(main(10))