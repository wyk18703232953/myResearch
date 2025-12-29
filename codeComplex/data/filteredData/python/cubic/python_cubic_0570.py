from copy import deepcopy
import random

def main(n: int):
    # 1. 生成规模为 n 的随机数字串 a 和 b（不含前导零）
    if n <= 0:
        return

    # 保证首位非零，长度为 n
    def gen_number_of_length(n):
        first = random.randint(1, 9)
        rest = [random.randint(0, 9) for _ in range(n - 1)]
        return [first] + rest

    # 这里按原程序逻辑，a 和 b 的长度相同（都为 n）
    a = gen_number_of_length(n)
    b = gen_number_of_length(n)

    # 2. 原始逻辑开始（移除了 input() 并封装为函数）

    cnt1 = [0] * 10
    cnt2 = [0] * 10
    ans = []

    if len(a) != len(b):
        print(''.join(map(str, sorted(a, reverse=True))))
        return

    for i in range(len(b) + 1):
        ok = 1
        tmp = deepcopy(a)
        for j in range(i):
            if b[j] in tmp:
                tmp.pop(tmp.index(b[j]))
            else:
                ok = 0
                break
        if not ok:
            continue

        pls = -1
        ind = -1
        if i < len(b):
            for j in range(len(tmp)):
                if tmp[j] < b[i]:
                    if tmp[j] > pls:
                        ind = j
                        pls = tmp[j]

        if pls == -1 and len(tmp) != 0 and i < len(b):
            continue
        else:
            if len(tmp) > 0 and ind != -1:
                tmp.pop(ind)
            if i == len(b):
                ans.append(''.join(map(str, b[:i])))
            else:
                ans.append(
                    ''.join(map(str, b[:i]))
                    + (str(pls) if pls != -1 else '')
                    + ''.join(map(str, sorted(tmp, reverse=True)))
                )

    print(max(ans))


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)