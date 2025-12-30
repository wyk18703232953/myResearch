#!/usr/bin/env python3

def solve(k: int) -> str:
    cmp = 9
    ndigit = 1

    while k > (cmp * ndigit):
        k -= cmp * ndigit
        cmp *= 10
        ndigit += 1

    num = (10 ** (ndigit - 1)) + ((k - 1) // ndigit)
    pos = (k - 1) % ndigit

    return str(num)[pos]


def main(n: int):
    """
    n: 规模参数，用于生成测试数据。
       这里约定：测试用例数量 t = n，
       第 i 个测试用例的 k = i。
    """
    t = n
    for i in range(1, t + 1):
        k = i  # 根据规模生成的第 i 个 k
        ans = solve(k)
        print(ans)


if __name__ == "__main__":
    # 示例：当规模为 10 时运行 main(10)
    main(10)