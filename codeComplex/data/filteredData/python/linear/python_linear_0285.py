import random

def main(n):
    # 生成 n 个只包含 '(' 和 ')' 的随机括号串
    # 每个串的长度在 1 到 max_len 之间随机
    max_len = 50
    strings = []
    for _ in range(n):
        length = random.randint(1, max_len)
        s = ''.join(random.choice('()') for _ in range(length))
        strings.append(s)

    c, r = 0, 0
    MAXN = 300000
    o = [0] * MAXN
    e = [0] * MAXN

    for s in strings:
        l = 0  # 未匹配左括号数量
        n_unmatched_right = 0  # 未匹配右括号数量
        for ch in s:
            if ch == '(':
                l += 1
            else:
                if l != 0:
                    l -= 1
                else:
                    n_unmatched_right += 1
        if l == 0 and n_unmatched_right == 0:
            c += 1
        elif l != 0 and n_unmatched_right != 0:
            pass
        elif l != 0:
            o[l] += 1
        else:
            e[n_unmatched_right] += 1

    for i in range(MAXN):
        if e[i] and o[i]:
            r += e[i] * o[i]

    print(pow(c, 2) + r)


if __name__ == '__main__':
    # 示例：运行规模为 1000
    main(1000)