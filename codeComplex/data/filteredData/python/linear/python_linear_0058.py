__author__ = 'ruckus'

import random
import string


def main(n):
    # 1. 生成测试数据：两个长度为 n 的字符串 s, t
    #   这里使用小写字母随机生成，你可按需要修改
    alphabet = string.ascii_lowercase
    s = ''.join(random.choice(alphabet) for _ in range(n))

    # 为了更有意义的测试，这里从 s 派生 t，使其有一定差异
    t_list = list(s)
    # 随机选择若干位置进行修改
    diff_positions = random.sample(range(n), k=random.randint(0, n))
    for pos in diff_positions:
        # 保证修改后字符不同
        original_char = t_list[pos]
        choices = [c for c in alphabet if c != original_char]
        t_list[pos] = random.choice(choices)
    t = ''.join(t_list)

    # 2. 原始逻辑
    dif = {}
    hem = 0
    for i in range(n):
        if s[i] != t[i]:
            dif[i] = [s[i], t[i]]
            hem += 1

    change = []
    probed = []
    k = 0
    for i in dif.keys():
        if dif[i] in probed:
            continue
        probed.append(dif[i])
        k += 1
        for j in list(dif.keys())[k:]:
            if dif[i] == dif[j][::-1]:
                print(hem - 2)
                print(i + 1, j + 1)
                return
            if not change and (dif[i][0] == dif[j][1] or dif[j][0] == dif[i][1]):
                change = [i, j]

    if change:
        print(hem - 1)
        print(change[0] + 1, change[1] + 1)
    else:
        print(hem)
        print('-1 -1')


if __name__ == "__main__":
    # 示例：n 可在此处修改或由外部调用 main(n)
    main(10)