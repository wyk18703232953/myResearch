import random

def f(i: int) -> int:
    s = 0
    while i > 0:
        s += i % 10
        i //= 10
    return s

def solve(n: int, s: int) -> int:
    sol = 0
    l = 1
    r = n
    while l <= r:
        i = (l + r) // 2
        digit_sum = f(i)

        if i - digit_sum >= s:
            sol = n - i + 1
            r = i - 1
        else:
            l = i + 1
    return sol

def main(n: int):
    # 根据规模 n 生成一个测试用的 s
    # 让 s 落在 [0, n] 范围内
    s = random.randint(0, n) if n > 0 else 0

    result = solve(n, s)
    print(result)

if __name__ == "__main__":
    # 示例: 传入一个固定的 n 以运行
    main(10**6)