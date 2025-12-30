import random

p = 10**9 + 7

def main(n):
    # 生成 n 组测试数据 (l, r)，保证 0 <= l <= r
    tests = []
    for _ in range(n):
        # 控制数值规模在 0 ~ 2^61 之间，覆盖原程序位运算范围
        x = random.randint(0, 2**61 - 1)
        y = random.randint(0, 2**61 - 1)
        l, r = (x, y) if x <= y else (y, x)
        tests.append((l, r))

    def solve(l, r):
        ans, a, b = 0, 0, 0
        mul = 2**60
        for _ in range(61):
            ch1, ch2 = 0, 0
            if a + mul <= l:
                a += mul
                ch1 = 1
            if b + mul <= l:
                b += mul
                ch2 = 1
            if ch1 ^ ch2 == 1:
                ans += mul
            elif ch1 == 0 and ch2 == 0:
                if a + mul <= r:
                    a += mul
                    ans += mul
                elif b + mul <= r:
                    b += mul
                    ans += mul
            mul //= 2
        return ans

    # 执行所有测试并输出
    for l, r in tests:
        print(l, r, solve(l, r))


if __name__ == "__main__":
    # 示例：生成并求解 n=5 组数据
    main(5)