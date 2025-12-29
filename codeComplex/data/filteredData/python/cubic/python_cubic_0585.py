import random
import string


def check(res, j, a, b):
    added = False
    tmp = ""
    for i in a:
        if i == j and not added:
            added = True
        else:
            tmp += i
    tmp = res + j + tmp[::-1]
    return tmp <= b


def main(n: int):
    """
    规模 n：生成两个长度为 n 的小写字母串 a, b，保持与原逻辑一致：
    若 len(a) < len(b) 的分支，用 len(a) < len(b) 的数据；
    否则用 len(a) == len(b) 的数据。
    """
    # 随机决定走哪个分支：0 -> len(a) < len(b), 1 -> len(a) == len(b)
    branch = random.randint(0, 1)

    if branch == 0:
        # len(a) < len(b)
        len_a = max(1, n - 1)  # 至少 1
        len_b = len_a + 1
    else:
        # len(a) == len(b)
        len_a = len_b = max(1, n)

    # 生成测试数据：小写字母串
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_a))
    b = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_b))

    # 原逻辑开始
    if len(a) < len(b):
        a_list = sorted(a)[::-1]
        res = ''.join(a_list)
        print(res)
        return

    # len(a) == len(b)
    res = ""
    n_len = len(a)
    a_list = sorted(list(a))[::-1]
    for _ in range(n_len):
        for j in a_list:
            if check(res, j, a_list, b):
                res += j
                a_list.remove(j)
                break
    print(res)


if __name__ == "__main__":
    # 示例：规模 5
    main(5)