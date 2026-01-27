def solve(a, b):
    if a == 0:
        return 0
    return b // a + solve(b % a, a)

def main(n):
    # 解释规模映射：
    # 使用 n 生成两个整数 a, b，保持规模在 O(n) 级别
    # 确定性构造：
    # a = n + 1 保证 a > 0
    # b = 2 * n + 1 保证 b >= a 对于 n >= 1
    if n <= 0:
        a = 1
        b = 1

    else:
        a = n + 1
        b = 2 * n + 1
    res = solve(a, b)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)