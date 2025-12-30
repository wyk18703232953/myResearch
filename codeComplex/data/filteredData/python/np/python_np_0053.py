import math
import random

def main(n: int):
    # 生成测试数据：
    # a 为长度 n，由 '+'、'-' 组成
    # b 为长度 n，由 '+','-','?' 组成（'?' 对应原来统计的 q）
    a = ''.join(random.choice(['+', '-']) for _ in range(n))
    b = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    c = 0
    d = 0
    q = 0

    for ch in a:
        if ch == '+':
            c += 1
        elif ch == '-':
            c -= 1

    for ch in b:
        if ch == '+':
            d += 1
        elif ch == '-':
            d -= 1
        else:
            q += 1

    if c == d:
        # c == d 时只需要所有 ? 的正负号刚好抵消
        # 注意 q/2 要为整数，这里 q 一定是整数，且只有在 q 偶数时组合数才非零
        if q % 2 != 0:
            print(0.0)
            return
        ways = math.factorial(q) // (math.factorial(q // 2) * math.factorial(q // 2))
        prob = ways / (2 ** q)
        print(prob)
    else:
        mx = d + q
        mn = d - q
        if c > mx or c < mn:
            print(0.0)
        else:
            ans = c - d  # 需要通过 ? 的分配来补足的差值
            # ans 的奇偶性必须与 q 同，使得 (q - ans) / 2 为整数
            if (q - abs(ans)) % 2 != 0 or abs(ans) > q:
                print(0.0)
                return

            if ans > 0:
                # 正数需要更多 '+'
                k_pos = (q - ans) // 2 + ans  # '+' 的个数
                k_neg = (q - ans) // 2        # '-' 的个数
            else:
                # 负数需要更多 '-'
                k_pos = (q - ans) // 2        # '+' 的个数
                k_neg = (q - ans) // 2 + ans  # '-' 的个数

            if k_pos < 0 or k_neg < 0 or k_pos + k_neg != q:
                print(0.0)
                return

            ways = math.factorial(q) // (math.factorial(k_pos) * math.factorial(k_neg))
            prob = ways / (2 ** q)
            print(prob)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)