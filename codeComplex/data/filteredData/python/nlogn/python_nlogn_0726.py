import random

def solve(a, b, c):
    if a == b and b == c:
        return 0
    elif a == b or b == c or a == c:
        return 1
    else:
        na = int(a[0])
        nb = int(b[0])
        nc = int(c[0])
        if a[1] == b[1] and a[1] == c[1]:
            cp = [na, nb, nc]
            cp.sort()
            cp[0] += 2
            cp[1] += 1
            if cp[0] == cp[1] and cp[1] == cp[2]:
                return 0
            elif (
                cp[0] == cp[1]
                or cp[1] == cp[2]
                or cp[0] == cp[1]
                or (cp[0] + 1) == cp[1]
                or (cp[1] + 1) == cp[2]
            ):
                return 1
            else:
                return 2
        elif a[1] == b[1]:
            mi = min(na, nb)
            ma = max(na, nb)
            if mi == (ma - 1) or mi == (ma - 2):
                return 1
            else:
                return 2
        elif a[1] == c[1]:
            mi = min(na, nc)
            ma = max(na, nc)
            if mi == (ma - 1) or mi == (ma - 2):
                return 1
            else:
                return 2
        elif b[1] == c[1]:
            mi = min(nb, nc)
            ma = max(nb, nc)
            if mi == (ma - 1) or mi == (ma - 2):
                return 1
            else:
                return 2
        else:
            return 2


def generate_tile():
    # 数字 1-9，花色从 'm','p','s' 中随机选择
    num = random.randint(1, 9)
    suit = random.choice(['m', 'p', 's'])
    return f"{num}{suit}"


def main(n):
    """
    n 为测试规模，这里生成 n 组 (a, b, c)，并输出对应结果。
    """
    random.seed(0)
    for _ in range(n):
        a = generate_tile()
        b = generate_tile()
        c = generate_tile()
        ans = solve(a, b, c)
        print(a, b, c, ans)


if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)