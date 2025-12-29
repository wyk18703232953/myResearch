import random
import string

def generate_test_data(n):
    """
    生成规模为 n 的测试数据：
    构造一个字符串链，每个字符串都是后一个字符串的子串，
    保证原算法在大多数情况下输出 YES。
    """
    s = []
    # 基础字符串
    base = ''.join(random.choices(string.ascii_lowercase, k=5))
    s.append(base)
    for _ in range(1, n):
        # 在前一个字符串基础上扩展，保证子串关系
        prev = s[-1]
        extra = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
        # 随机插入位置
        pos = random.randint(0, len(prev))
        new_str = prev[:pos] + extra + prev[pos:]
        s.append(new_str)
    # 打乱顺序，模拟原始输入无序情况
    random.shuffle(s)
    return s

def main(n):
    # 生成测试数据
    s = generate_test_data(n)

    # 原逻辑开始
    a = sorted(s, key=len)
    c = 1
    for i in range(n - 1):
        if a[i] not in a[i + 1]:
            c = 0
            break
    if c == 0:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            print(a[i])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)