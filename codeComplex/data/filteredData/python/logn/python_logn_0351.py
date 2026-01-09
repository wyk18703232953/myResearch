import math

mod = 10**9 + 7

def calcpower(num, power, mod):
    """
    raises the num to the power power
    """
    if power == 0:
        return 1

    a = [num]
    temp = num
    for _ in range(int(math.log(power, 2))):
        temp *= temp
        temp %= mod
        a.append(temp % mod)

    power_bin = bin(power)[2:][::-1]

    res = 1
    for i in range(len(power_bin)):
        if int(power_bin[i]):
            res = (res * a[i]) % mod
    return res % mod


def main(n):
    """
    n 作为规模参数，这里用来生成测试数据 (x, k)。
    示例策略：
    - x = n
    - k = n
    可根据需要调整生成方式。
    """
    x = n
    k = n

    if x == 0:
        return 0
    if k == 0:
        return 2 * x % mod

    ans = (2 * x - 1) * calcpower(2, k, mod) + 1
    return ans % mod


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    # print(main(10))
    pass