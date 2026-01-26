def solve(x, y, n):
    return "White" if (x - 1 + y - 1) <= (n - x + n - y) else "Black"


def main(n):
    # 将 n 视为棋盘大小，构造一个确定性的 (x, y)
    if n <= 0:
        return
    x = (n // 2) + 1 if n % 2 == 0 else (n // 2 + 1)
    y = (n * 2 // 3) + 1
    if y > n:
        y = n
    result = solve(x, y, n)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)