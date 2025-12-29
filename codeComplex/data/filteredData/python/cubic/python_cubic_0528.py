from collections import Counter
import random


def mx(f):
    res = []
    for k in sorted(f.keys(), reverse=True):
        for _ in range(f[k]):
            res.append(k)
    return res


def solve(n, a, b):
    res = None
    for k in range(n + 1):
        aa = Counter(a)
        cur = []
        for i in range(k):
            if aa[b[i]] == 0:
                return res
            cur.append(b[i])
            aa[b[i]] -= 1
        if k < n:
            for e in range(b[k] - 1, -1, -1):
                if aa[e] > 0:
                    cur.append(e)
                    aa[e] -= 1
                    cur.extend(mx(aa))
                    break
            if len(cur) < n:
                continue
        res = cur
    return res


def generate_test_data(n):
    """
    生成规模为 n 的测试数据:
    - a_str: 由数字字符组成的字符串，其长度在 [n, 2n] 区间内
    - b_str: 长度为 n 的数字字符字符串
    """
    # 确保 a 的长度至少为 n，至多为 2n
    len_a = random.randint(max(1, n), max(1, 2 * n))
    a_digits = [str(random.randint(0, 9)) for _ in range(len_a)]
    b_digits = [str(random.randint(0, 9)) for _ in range(max(1, n))]
    a_str = ''.join(a_digits)
    b_str = ''.join(b_digits)
    return a_str, b_str


def main(n):
    # 生成测试数据
    a_str, b_str = generate_test_data(n)

    # 将原始逻辑参数化
    a = Counter(map(int, a_str))
    b = list(map(int, b_str))

    if sum(a.values()) < len(b):
        res = mx(a)
    else:
        res = solve(len(b), a, b)

    # 输出结果
    print(''.join(map(str, res)))


if __name__ == "__main__":
    # 示例：可修改 n 以改变测试规模
    main(10)