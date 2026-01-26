from math import sqrt

mod = 10 ** 9 + 7
mod2 = 998244353

S1 = 'abcdefghijklmnopqrstuvwxyz'
S2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def isprime(x):
    if x <= 1:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def main(n):
    """
    根据规模 n 生成 (n, k) 并计算原程序结果。
    这里设 k = n（可根据需要修改生成规则）。
    返回值为原程序最终输出。
    """
    k = n  # 测试数据生成规则：k 与 n 相同

    if n == 0:
        return 0

    x = (n * pow(2, k + 1, mod)) % mod
    return (x - pow(2, k, mod) + 1) % mod


if __name__ == "__main__":
    # 示例：调用 main(5)，可自行修改或在其他文件中导入调用
    # print(main(5))
    pass