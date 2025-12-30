import sys
import random

def solve(k: int) -> str:
    if not isinstance(k, int) or k <= 0 or k > 10**12:
        return "wrong input. try again"

    lim_init = lim = decimal = 9
    c = 0
    while True:
        c += 1
        if k <= lim:
            diff = lim - k
            pos = diff % c
            diff //= c
            diff = decimal - diff
            return ''.join(reversed(str(diff)))[pos]
        else:
            decimal = int(str(lim_init) * (c + 1))
            lim += int(str(lim_init) + '0' * c) * (c + 1)


def main(n: int):
    # 生成 n 个测试数据并输出结果
    # 按原程序约束：1 <= k <= 1e12
    for _ in range(n):
        k = random.randint(1, 10**12)
        res = solve(k)
        # 只输出原逻辑结果（不带测试数据 k）
        sys.stdout.write(str(res) + "\n")


if __name__ == "__main__":
    # 示例：规模 n = 5，可按需修改
    main(5)