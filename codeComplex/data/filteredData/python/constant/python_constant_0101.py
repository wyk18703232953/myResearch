import math

def main(n):
    # n 表示测试用例数量
    for i in range(n):
        a = i + 2
        b = 2 * i + 3
        ans = 0
        x, y = a, b
        while x > 0 and y > 0:
            if x >= y:
                ans += x // y
                x = x % y

            else:
                ans += y // x
                y = y % x
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)