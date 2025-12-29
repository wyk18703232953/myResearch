from collections import defaultdict
import random
import string

def main(n):
    # 生成测试数据：长度为 n 的字符串 s 和 t
    # 字符集可自行调整，这里使用小写字母
    alphabet = string.ascii_lowercase

    # 随机生成 s 和 t，可以按需要保证一定数量的不相同位置
    s = ''.join(random.choice(alphabet) for _ in range(n))
    t = list(s)

    # 为了保证有一定数量的不同位置，随机选择若干位置进行修改
    # 修改数量在 [0, n] 范围内
    diff_cnt = random.randint(0, n)
    positions = random.sample(range(n), diff_cnt) if diff_cnt <= n else list(range(n))
    for pos in positions:
        # 确保 t[pos] != s[pos]
        choices = [c for c in alphabet if c != s[pos]]
        t[pos] = random.choice(choices)
    t = ''.join(t)

    # 以下为原逻辑（去掉 input()，用生成的 s, t 替代）
    value = {}
    li = []
    res1 = 0
    res2 = res3 = -1

    for i in range(n):
        if s[i] != t[i]:
            value[t[i]] = i
            res1 += 1
            li.append(i)

    p = sq = False
    for i in li:
        if s[i] in value:
            p = True
            res2 = i + 1
            f = value[s[i]]
            res3 = f + 1
            if s[f] == t[i]:
                sq = True
                break

    print(res1 - (2 if sq else 1 if p else 0))
    print(res2, res3)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)