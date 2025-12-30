def main(n):
    # 为了演示，将 a,b 固定为题目中常见的两种情况之一。
    # 这里约定：若 n 为偶数则使用 a=1,b=2；若 n 为奇数则使用 a=1,b=1。
    if n <= 0:
        return

    if n % 2 == 0:
        a, b = 1, 2
    else:
        a, b = 1, 1

    if min(a, b) != 1:
        print("NO")
        return
    if a == b == 1 and n in (2, 3):
        print("NO")
        return

    print("YES")
    ONE, ZERO = ("10" if a > 1 else "01")

    edges = n - max(a, b)
    line = "0" + (ZERO, ONE)[edges > 0] * (n > 1) + ZERO * (n - 2)
    print(line)

    for y in range(1, n):
        line = ZERO * (y - 1) + (ZERO, ONE)[y <= edges] + "0"
        if y < n - 1:
            line += (ZERO, ONE)[y < edges] + ZERO * (n - y - 2)
        print(line)