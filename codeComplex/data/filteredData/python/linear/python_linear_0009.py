import random
import string

def excel_to_rc(s: str) -> str:
    # e.g., "BC23" -> "R23C55"
    c = 0
    p = 0
    while p < len(s) and not s[p].isdigit():
        c = c * 26 + (ord(s[p]) - ord('A') + 1)
        p += 1
    r = s[p:]
    return f"R{r}C{c}"

def rc_to_excel(s: str) -> str:
    # e.g., "R23C55" -> "BC23"
    v = []

    p = s.find('C')
    r = int(s[1:p])
    c = int(s[p + 1:])

    while c > 0:
        if c % 26 == 0:
            v.append('Z')
            c = (c - 1) // 26
        else:
            v.append(chr(ord('A') + (c % 26 - 1)))
            c //= 26

    v.reverse()
    return f"{''.join(v)}{r}"

def gen_rc() -> str:
    # 生成 RC 格式：R<row>C<col>
    row = random.randint(1, 10**6)
    col = random.randint(1, 10**6)
    return f"R{row}C{col}"

def gen_excel() -> str:
    # 生成 Excel 格式：<col letters><row>
    col_num = random.randint(1, 10**6)
    row = random.randint(1, 10**6)
    letters = []
    c = col_num
    while c > 0:
        if c % 26 == 0:
            letters.append('Z')
            c = (c - 1) // 26
        else:
            letters.append(chr(ord('A') + (c % 26 - 1)))
            c //= 26
    letters.reverse()
    return f"{''.join(letters)}{row}"

def gen_test_string() -> str:
    # 随机生成 RC 或 Excel 格式
    if random.choice([True, False]):
        return gen_rc()
    else:
        return gen_excel()

def main(n: int):
    random.seed(0)  # 如需可重复性
    for _ in range(n):
        s = gen_test_string()
        p = s.find('C')
        # 模拟原逻辑的判断
        if s[0] == 'R' and len(s) > 1 and s[1].isdigit() and p > 1:
            # RC -> Excel
            out = rc_to_excel(s)
        else:
            # Excel -> RC
            out = excel_to_rc(s)
        print(out)

if __name__ == "__main__":
    main(10)