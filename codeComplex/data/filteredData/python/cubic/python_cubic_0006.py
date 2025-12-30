import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字母串
    #    若需要其他生成方式，可自行修改此部分
    letters = string.ascii_lowercase
    s = [random.choice(letters) for _ in range(n)]

    # 原逻辑开始
    if len(set(s)) == len(s):
        print('0')
        return

    d = []

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            x = ''
            for k in range(i, j + 1):
                x += s[k]
            d.append(x)

    v = {}
    for i in range(len(s)):
        if s[i] not in v:
            v[s[i]] = 1
        else:
            v[s[i]] += 1

    for i in d:
        if i not in v:
            v[i] = 1
        else:
            v[i] += 1

    mx = -1

    for i in v:
        if v[i] >= 2:
            if len(i) > mx:
                mx = max(mx, len(i))

    print(mx)


if __name__ == "__main__":
    # 示例运行：n = 10
    main(10)