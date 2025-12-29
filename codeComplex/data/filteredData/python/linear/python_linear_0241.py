import random
import string

def main(n: int):
    # 生成测试数据
    # turns: 1 到 n 之间
    turns = random.randint(1, max(1, n))

    # 字符串长度与 n 相关，这里设为 n，字符来自大小写字母
    alphabet = string.ascii_uppercase + string.ascii_lowercase

    def gen_string(length):
        return ''.join(random.choice(alphabet) for _ in range(length))

    s0 = gen_string(n)
    s1 = gen_string(n)
    s2 = gen_string(n)

    # 原逻辑开始
    d0 = {char: 0 for char in alphabet}
    d1 = {char: 0 for char in alphabet}
    d2 = {char: 0 for char in alphabet}

    for char in s0:
        d0[char] += 1
    for char in s1:
        d1[char] += 1
    for char in s2:
        d2[char] += 1

    m0 = max(d0[char] for char in alphabet)
    m1 = max(d1[char] for char in alphabet)
    m2 = max(d2[char] for char in alphabet)

    l0 = len(s0)
    l1 = len(s1)
    l2 = len(s2)

    if turns == 1 and m0 == l0:
        score0 = m0 - 1
    else:
        score0 = min(l0, m0 + turns)

    if turns == 1 and m1 == l1:
        score1 = m1 - 1
    else:
        score1 = min(l1, m1 + turns)

    if turns == 1 and m2 == l2:
        score2 = m2 - 1
    else:
        score2 = min(l2, m2 + turns)

    scores = [score0, score1, score2]
    bestscore = max(scores)

    winnerlist = [i for i in range(3) if scores[i] == bestscore]
    if len(winnerlist) > 1:
        print('Draw')
    else:
        print(['Kuro', 'Shiro', 'Katie'][winnerlist[0]])


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)