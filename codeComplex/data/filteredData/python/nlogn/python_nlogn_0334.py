import random
import string

def generate_test_data(n):
    """
    生成满足原题语义的字符串列表 a，长度为 n。
    生成方式：
    - 从一个基础字符串开始
    - 逐步在其前后或中间插入随机字符，形成包含关系链
    这样保证 a 按长度排序后满足 a[i-1] 为 a[i] 的子串。
    """
    if n <= 0:
        return []

    # 随机生成一个基础字符串，长度 1~5
    base_len = random.randint(1, 5)
    base = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))

    a = [base]
    cur = base
    for _ in range(1, n):
        # 在当前字符串的随机位置插入 1~3 个随机字符
        insert_count = random.randint(1, 3)
        s = cur
        for _ in range(insert_count):
            pos = random.randint(0, len(s))
            ch = random.choice(string.ascii_lowercase)
            s = s[:pos] + ch + s[pos:]
        a.append(s)
        cur = s

    # 打乱顺序以模拟无序输入
    random.shuffle(a)
    return a


def main(n):
    a = generate_test_data(n)

    if n == 1:
        print("YES")
        print(a[0])
        return

    a.sort(key=len)
    for i in range(1, n):
        if a[i - 1] not in a[i]:
            print("NO")
            return

    print("YES")
    for s in a:
        print(s)


if __name__ == "__main__":
    # 示例运行：可自行修改 n
    main(5)