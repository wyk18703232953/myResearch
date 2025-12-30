import random
import string

def convert_rc_to_bc(s: str) -> str:
    # R23C55 -> BC23
    p = s.find('C')
    r = int(s[1:p])
    c = int(s[p + 1:])

    v = []
    while c > 0:
        if c % 26 == 0:
            v.append('Z')
            c = (c - 1) // 26
        else:
            v.append(chr(ord('A') + (c % 26 - 1)))
            c //= 26

    v.reverse()
    return f"{''.join(v)}{r}"


def convert_bc_to_rc(s: str) -> str:
    # BC23 -> R23C55
    p = 0
    while p < len(s) and not s[p].isdigit():
        p += 1

    sr = s[:p]
    sc = s[p:]

    c = 0
    for x in sr:
        c = c * 26 + (ord(x) - ord('A') + 1)

    return f"R{sc}C{c}"


def generate_rc_style(max_row: int = 10**6, max_col: int = 10**6) -> str:
    r = random.randint(1, max_row)
    c = random.randint(1, max_col)
    return f"R{r}C{c}"


def generate_bc_style(max_row: int = 10**6, max_col: int = 10**6) -> str:
    # 生成列号 -> 字母
    c = random.randint(1, max_col)
    v = []
    x = c
    while x > 0:
        if x % 26 == 0:
            v.append('Z')
            x = (x - 1) // 26
        else:
            v.append(chr(ord('A') + (x % 26 - 1)))
            x //= 26
    v.reverse()
    col_letters = ''.join(v)

    r = random.randint(1, max_row)
    return f"{col_letters}{r}"


def main(n: int):
    random.seed(0)
    for _ in range(n):
        # 随机选择生成 RC 风格或 BC 风格字符串
        if random.choice([True, False]):
            s = generate_rc_style()
            print(convert_rc_to_bc(s))
        else:
            s = generate_bc_style()
            print(convert_bc_to_rc(s))


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)