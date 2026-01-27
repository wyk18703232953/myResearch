#!/usr/bin/env python3

def solve(k: int) -> str:
    cmp_val = 9
    ndigit = 1

    while k > (cmp_val * ndigit):
        k -= cmp_val * ndigit
        cmp_val *= 10
        ndigit += 1

    num = (10 ** (ndigit - 1)) + ((k - 1) // ndigit)
    pos = (k - 1) % ndigit

    return str(num)[pos]


def main(n: int):
    """
    n 作为规模参数，用于生成测试数据：
    - 假设有 n 个测试用例
    - 第 i 个测试用例的 k = i（即查找整个数字序列中第 i 位的数字）
    """
    tcs = n
    for tc in range(1, tcs + 1):
        k = tc  # 简单按序生成测试数据
        ans = solve(k)
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：当 n = 10 时，生成并求解 10 个测试用例
    main(10)