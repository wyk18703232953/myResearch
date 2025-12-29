import random
import string

def generate_test_data(n):
    """
    生成满足/不满足条件的随机字符串列表：
    条件：可重排后按长度排序，使得每个 s[i-1] 是 s[i] 的子串。
    这里生成“肯定满足条件”的数据，保证程序输出 YES。
    """
    strings = []

    # 生成一个初始随机字符串
    base_len = random.randint(1, 5)
    base = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))
    strings.append(base)

    # 逐步在前一个字符串基础上扩展，保证子串关系
    for _ in range(1, n):
        prev = strings[-1]
        # 随机插入一些字符，保证 prev 为新串的子串
        extra_len = random.randint(0, 5)
        extra = ''.join(random.choice(string.ascii_lowercase) for _ in range(extra_len))
        # 将 prev 嵌入到新串中
        pos = random.randint(0, len(extra))
        new_s = extra[:pos] + prev + extra[pos:]
        strings.append(new_s)

    # 打乱顺序，模拟原题任意输入
    random.shuffle(strings)
    return strings

def main(n):
    l = generate_test_data(n)
    s = sorted(l, key=len)
    for i in range(1, n):
        if s[i - 1] not in s[i]:
            print("NO")
            return
    print("YES")
    for x in s:
        print(x)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值
    main(5)