from random import randint

MOD = 1000000007

def binary_exp(x, n, prime):
    if n == 0:
        return 1
    elif n == 1:
        return x % prime
    else:
        temp = binary_exp(x, n // 2, prime)
        temp = (temp * temp) % prime
        if n % 2 == 0:
            return temp
        else:
            return ((x % prime) * temp) % prime

def solve(x, k):
    if x == 0:
        return 0
    val1 = binary_exp(2, k + 1, MOD)
    val2 = binary_exp(2, k, MOD)
    ans = ((val1 * (x % MOD)) % MOD - (val2 - 1) % MOD) % MOD
    return ans

def main(n):
    # 根据规模 n 生成测试数据
    # 示例：生成 1 组 (x, k)，x, k 的上界随 n 增大
    x = randint(0, 10 ** max(1, min(9, n)))   # 控制在合理范围内
    k = randint(0, 10 ** max(1, min(6, n)))   # 避免指数过大导致时间过长

    result = solve(x, k)
    print(result)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)