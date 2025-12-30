import random

def main(n: int):
    # 生成一个 n 位的正整数 a（首位不为 0）
    if n <= 0:
        return

    first_digit = random.randint(1, 9)
    other_digits = [random.randint(0, 9) for _ in range(n - 1)]
    digits = [first_digit] + other_digits
    a = 0
    for d in digits:
        a = a * 10 + d

    # 原逻辑开始：根据 n 和生成的 a 判断输出 YES/NO
    s = 0
    t = a
    b = []
    for _ in range(n):
        s += t % 10
        b.append(t % 10)
        t //= 10
    b.reverse()

    i = 2
    ans = False
    if s == 0:
        ans = True

    while i <= s:
        if s % i != 0:
            i += 1
            continue
        l = s // i
        c = 0
        su = 0
        for j in range(n):
            if su > l:
                break
            else:
                su += b[j]
                if su == l:
                    su = 0
                    c += 1
        if c == i:
            ans = True
        i += 1

    if ans:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次规模为 5 的测试
    main(5)