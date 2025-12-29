import random
import string

def generate_test_data(n: int):
    """
    生成 n 个字符串，构造方式保证它们两两之间存在包含关系，
    以尽量产生 'YES' 情况（可根据需要修改生成策略）。
    """
    if n <= 0:
        return []

    # 生成一个基础字符串
    base_len = max(1, n // 2)
    base = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))

    s = [base]

    # 生成其它字符串，随机在 base 的基础上加前缀/后缀或取子串等
    for _ in range(n - 1):
        op = random.choice(['prefix', 'suffix', 'sub', 'extend'])
        if op == 'prefix':
            extra = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 3)))
            s.append(extra + base)
        elif op == 'suffix':
            extra = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 3)))
            s.append(base + extra)
        elif op == 'sub' and len(base) > 1:
            l = random.randint(1, len(base))
            start = random.randint(0, len(base) - l)
            s.append(base[start:start + l])
        else:  # extend
            extra1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(0, 2)))
            extra2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(0, 2)))
            s.append(extra1 + base + extra2)

    return s

def main(n: int):
    # 1. 根据 n 生成测试数据
    s = generate_test_data(n)

    # 2. 按原逻辑进行判断和输出
    for i in s:
        for j in s:
            if (i not in j) and (j not in i):
                print('NO')
                return

    print('YES')
    s_sorted = sorted(s, key=lambda x: len(x))
    for pal in s_sorted:
        print(pal)

if __name__ == "__main__":
    # 示例：n = 5
    main(5)