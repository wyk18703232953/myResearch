import random

def solve(L, R):
    if L == R:
        return 0
    l = len(bin(L)[2:])
    r = len(bin(R)[2:])
    while l == r:
        L -= pow(2, r - 1)
        R -= pow(2, r - 1)
        l = len(bin(L)[2:])
        r = len(bin(R)[2:])
    return pow(2, r) - 1

def main(n):
    """
    n 作为规模参数，用于生成测试数据。
    这里设定：
      - 生成一组 (L, R)
      - 0 <= L <= R < 2^n
    """
    if n <= 0:
        n = 1
    max_val = (1 << n) - 1

    # 生成随机 L, R，保证 L <= R
    L = random.randint(0, max_val)
    R = random.randint(L, max_val)

    ans = solve(L, R)
    print(ans)

if __name__ == "__main__":
    # 可以在这里修改 n 进行本地测试
    main(10)