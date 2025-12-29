import random

# 模拟交互器：隐藏的 a, b
hidden_a = 0
hidden_b = 0

def comparator(x: int, y: int) -> int:
    """
    模拟原来交互里的返回值：
    返回 sign( (a ^ x) - (b ^ y) )
    >0 -> 1, <0 -> -1, ==0 -> 0
    """
    global hidden_a, hidden_b
    v1 = hidden_a ^ x
    v2 = hidden_b ^ y
    if v1 == v2:
        return 0
    return 1 if v1 > v2 else -1


def solve() -> tuple[int, int]:
    c, d = 0, 0
    ans = comparator(c, d)
    if ans == 0:
        # both numbers are equal
        num = 0
        for i in range(29, -1, -1):
            c = 1 << i
            d = 0
            ans = comparator(c, d)
            if ans == -1:
                num += (1 << i)
        return num, num
    else:
        l = [0, 0]
        if ans == 1:
            cur = 0
        else:
            cur = 1

        prev = ans
        # first find set of mutually exclusive bits
        for i in range(29, -1, -1):
            tc = c | (1 << i)
            td = d | (1 << i)
            ans = comparator(tc, td)
            if ans == 0:
                break
            if ans != prev:
                l[cur] += (1 << i)
                if cur == 0:
                    c = tc
                else:
                    d = td
                temp = comparator(c, d)
                prev = temp
                if temp == 1:
                    cur = 0
                else:
                    cur = 1
        c = l[0]
        d = l[1]
        # now try to find common bits
        for i in range(29, -1, -1):
            if (c & (1 << i)) != 0 or (d & (1 << i)) != 0:
                continue
            tc = c | (1 << i)
            ans = comparator(tc, d)
            if ans == -1:
                l[0] |= (1 << i)
                l[1] |= (1 << i)
        return l[0], l[1]


def main(n: int) -> None:
    """
    n 为规模，用来生成测试数据：
    - 随机生成 0 <= a, b < 2^n
    - 然后用改写后的算法推回 a, b 并打印
    """
    global hidden_a, hidden_b
    if n <= 0:
        n = 1
    if n > 30:
        n = 30  # 原算法只用到 0..29 位

    max_val = 1 << n
    hidden_a = random.randrange(0, max_val)
    hidden_b = random.randrange(0, max_val)

    x, y = solve()

    print("hidden_a:", hidden_a)
    print("hidden_b:", hidden_b)
    print("recovered:", x, y)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)