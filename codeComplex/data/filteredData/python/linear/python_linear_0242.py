from collections import Counter

def generate_strings(n):
    if n <= 0:
        n = 1
    # 第一串：全是同一字符，考察极端计数情况
    a = "a" * n
    # 第二串：周期性三种字符，长度略大于 n
    b = "".join(chr(ord('a') + (i % 3)) for i in range(n + 1))
    # 第三串：从 'a' 开始递增到 'z'，再循环，长度为 2n
    c = "".join(chr(ord('a') + (i % 26)) for i in range(2 * n))
    return a, b, c

def solve_game(n, a, b, c):
    fa = Counter(a)
    fb = Counter(b)
    fc = Counter(c)

    la = min(fa.most_common(1)[0][1] + n, len(a))
    lb = min(fb.most_common(1)[0][1] + n, len(a))
    lc = min(fc.most_common(1)[0][1] + n, len(a))

    if fa.most_common(1)[0][1] == len(a) and n == 1:
        la = len(a) - 1

    if fb.most_common(1)[0][1] == len(b) and n == 1:
        lb = len(b) - 1

    if fc.most_common(1)[0][1] == len(c) and n == 1:
        lc = len(c) - 1

    if la > max(lb, lc):
        return "Kuro"
    elif lb > max(la, lc):
        return "Shiro"
    elif lc > max(la, lb):
        return "Katie"
    else:
        return "Draw"

def main(n):
    a, b, c = generate_strings(n)
    result = solve_game(n, a, b, c)
    print(result)

if __name__ == "__main__":
    main(5)