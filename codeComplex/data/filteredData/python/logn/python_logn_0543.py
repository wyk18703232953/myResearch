import bisect
import random

xyz = [9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000, 9000000000, 900000000000]
xzy = [10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8888888890, 98888888890,
       1088888888890, 11888888888890]


def solve(k: int) -> str:
    digits = bisect.bisect_left(xzy, k)
    if k == 10:
        return "1"
    elif k > 10:
        apu = k - xzy[digits - 1]
        modulo = apu % (digits + 1)
        dlj = apu // (digits + 1)
        output = 10 ** digits + dlj
        list1 = [ch for ch in str(output)]
        return list1[modulo]
    else:
        return str(k)


def main(n: int):
    """
    使用规模 n 生成测试数据，并调用原逻辑。
    这里生成一个 1 到 n 之间的随机整数 k，作为原程序的 input().
    """
    if n <= 0:
        return

    # 生成测试数据：k 在 [1, n] 范围内
    k = random.randint(1, n)
    ans = solve(k)
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=100
    main(100)