import random
import string

def generate_test_strings(n):
    """
    生成 n 个字符串，构造方式：
    - 保证它们按长度非递减，以增加前缀/子串关系出现的概率
    - 字符集使用小写字母
    """
    strings = []
    base = ""
    for i in range(n):
        # 随机决定：在已有 base 上扩展，或重新开始一个新串
        if i == 0 or random.random() < 0.3:
            # 从头生成一个新串，长度在 1~(i+2) 之间，控制整体长度增长速度
            length = random.randint(1, i + 2)
            s = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
            base = s
        else:
            # 在当前 base 后面追加若干字符，构造包含关系
            extra_len = random.randint(1, 3)
            extra = "".join(random.choice(string.ascii_lowercase) for _ in range(extra_len))
            base = base + extra
            s = base
        strings.append(s)

    return strings


def main(n):
    # 1. 生成测试数据
    li = generate_test_strings(n)

    # 2. 原始逻辑
    lst2 = sorted(li, key=len)
    c = 1
    for i in range(len(lst2) - 1):
        if lst2[i] not in lst2[i + 1]:
            c = 0

    # 3. 输出
    if c == 1:
        print("YES")
        for j in lst2:
            print(j)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)