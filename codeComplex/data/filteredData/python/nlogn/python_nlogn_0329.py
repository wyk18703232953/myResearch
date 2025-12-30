import random
import string

def generate_test_data(n):
    """
    生成 n 个字符串，使其按长度排序后较短的往往是较长的子串，
    以提高满足条件的概率。
    """
    strings = []
    # 先生成一个基础长串
    base_len = max(1, n) * 3
    base = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))
    strings.append(base)

    # 生成其余串，其中大部分为 base 的子串，也掺杂一些随机串
    for _ in range(n - 1):
        if random.random() < 0.7:  # 70% 概率为 base 子串
            l = random.randint(1, len(base))
            start = random.randint(0, len(base) - l)
            s = base[start:start + l]
        else:  # 30% 概率为完全随机串
            l = random.randint(1, base_len)
            s = ''.join(random.choice(string.ascii_lowercase) for _ in range(l))
        strings.append(s)

    return strings


def main(n):
    # 生成测试数据
    data = generate_test_data(n)

    # 保持与原逻辑一致：按长度排序
    a = sorted(data, key=lambda x: len(x))
    v = all(a[i] in a[i + 1] for i in range(n - 1))

    if v:
        print("YES")
        print("\n".join(a))
    else:
        print("NO")


if __name__ == "__main__":
    # 这里给一个默认规模示例，可按需修改或在外部调用 main(n)
    main(5)