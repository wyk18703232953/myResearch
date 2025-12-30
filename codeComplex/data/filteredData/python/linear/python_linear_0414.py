import random
import string

def main(n, k=None, seed=0):
    """
    n: 字符串长度规模
    k: 题目中的参数，如果为 None，则随机生成 [1, min(26, n)] 之间的值
    seed: 随机种子，便于复现实验
    """
    random.seed(seed)

    # 生成测试数据：长度为 n 的小写字母字符串
    if n <= 0:
        print(-1)
        return

    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 若未指定 k，则随机生成
    if k is None:
        k = random.randint(1, min(26, n))

    # 原逻辑开始
    l = []
    for ch in s:
        val = ord(ch) - 96  # 'a' -> 1, 'b' -> 2, ...
        if val not in l:
            l.append(val)
    l.sort()

    if not l:
        print(-1)
        return

    c = l[0]
    a = 1
    b = l[0]

    for i in range(1, len(l)):
        if a == k:
            break
        if (l[i] - b) > 1:
            a += 1
            c += l[i]
            b = l[i]

    if a < k:
        print(-1)
    else:
        print(c)


if __name__ == "__main__":
    # 示例调用：n=10，k 未指定则随机
    main(10)