import random
import string

def generate_test_data(n):
    """
    生成满足/不完全满足条件的字符串列表：
    - 先生成一个基础字符串 base
    - 之后的字符串都是 base 的超串（包含 base）
    - 为了可能出现 NO 情况，随机打乱顺序
    """
    random.seed(0)

    # 生成一个长度适中的基础字符串
    base_len = max(1, n // 3)
    base = ''.join(random.choices(string.ascii_lowercase, k=base_len))

    strings = [base]
    for i in range(1, n):
        # 在 base 的基础上随机插入字符，生成超串
        extra_len = random.randint(0, 5)
        extras = ''.join(random.choices(string.ascii_lowercase, k=extra_len))
        pos = random.randint(0, len(base))
        s = base[:pos] + extras + base[pos:]
        strings.append(s)

    # 打乱顺序，避免已经按长度排序
    random.shuffle(strings)
    return strings

def main(n: int):
    l = generate_test_data(n)

    l.sort(key=lambda x: len(x))

    ok = True
    for i in range(n - 1):
        if l[i] not in l[i + 1]:
            ok = False
            break

    if ok:
        print("YES")
        print(*l, sep='\n')
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)