from collections import Counter
import random
import string


def main(n: int):
    # 生成测试数据：两个长度为 n 的字符串列表 A 和 B
    # 字符串由小写字母组成，长度为 1~5
    def random_str(min_len=1, max_len=5):
        length = random.randint(min_len, max_len)
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    A = [random_str() for _ in range(n)]
    B = [random_str() for _ in range(n)]

    a = Counter()
    b = Counter()

    for s in A:
        a[s] += 1
    for s in B:
        b[s] += 1

    ans = 0
    for key in b:
        ans += max(b[key] - a[key], 0)

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)