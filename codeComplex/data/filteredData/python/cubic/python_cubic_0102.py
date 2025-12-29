mod = 998244353
MAX_LENGTH = 20
bound = [0] * MAX_LENGTH

def mul(a, b):
    return (a * b) % mod

def add(a, b):
    a += b
    if a < 0:
        a += mod
    if a >= mod:
        a -= mod
    return a

def digitize(num):
    for i in range(MAX_LENGTH):
        bound[i] = num % 10
        num //= 10

def rec(smaller, start, pos, mask):
    global k, dp, bit_count, ten_pow
    if bit_count[mask] > k:
        return [0, 0]
    if pos == -1:
        return [0, 1]

    if dp[smaller][start][pos][mask][0] != -1:
        return dp[smaller][start][pos][mask]

    res_sum = 0
    res_ways = 0
    for digit in range(10):
        if smaller == 0 and digit > bound[pos]:
            continue
        new_smaller = smaller | (digit < bound[pos])
        new_start = start | (digit > 0) | (pos == 0)
        new_mask = (mask | (1 << digit)) if new_start == 1 else 0

        cur_sum, cur_ways = rec(new_smaller, new_start, pos - 1, new_mask)
        res_sum = add(res_sum, add(mul(mul(digit, ten_pow[pos]), cur_ways), cur_sum))
        res_ways = add(res_ways, cur_ways)

    dp[smaller][start][pos][mask][0] = res_sum
    dp[smaller][start][pos][mask][1] = res_ways
    return dp[smaller][start][pos][mask]

def solve(upper_bound):
    global dp
    dp = [[[[[-1, -1] for _ in range(1 << 10)]
             for _ in range(MAX_LENGTH)]
             for _ in range(2)]
             for _ in range(2)]
    digitize(upper_bound)
    ans = rec(0, 0, MAX_LENGTH - 1, 0)
    return ans[0]

def main(n):
    """
    n 为规模参数，这里用来构造测试数据：
    l = 1
    r = 10**n - 1
    k = n % 11   （使得 k 在 0..10 之间变化）

    返回原程序对区间 [l, r] 的答案。
    """
    global k, bit_count, ten_pow

    # 构造测试数据
    l = 1
    r = 10 ** n - 1
    k = n % 11

    # 预处理 bit_count
    bit_count = [0] * (1 << 10)
    for i in range(1, 1 << 10):
        bit_count[i] = bit_count[i & (i - 1)] + 1

    # 预处理 10 的幂
    ten_pow = [1]
    for _ in range(MAX_LENGTH):
        ten_pow.append(mul(ten_pow[-1], 10))

    ans = add(solve(r), -solve(l - 1))
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：使用 n = 5 运行
    main(5)