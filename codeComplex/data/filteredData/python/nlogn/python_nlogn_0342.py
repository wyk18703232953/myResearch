import random
import string

def main(n: int):
    # 1. 生成规模为 n 的测试数据：n 个随机字符串
    # 字符串长度在 1~10 之间，字符为小写字母
    uk = []
    for _ in range(n):
        length = random.randint(1, 10)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        uk.append(s)

    # 2. 以下为原代码逻辑（去除所有 input()，用生成的 uk 替代）

    gh = 0
    uo = 0
    # 原代码中这段逻辑只用于计算最长字符串及其下标，但后续未使用 uo
    for i in range(n):
        yu = uk[i]
        if len(yu) > gh:
            gh = len(yu)
            uo = i

    yk = 0
    yj = {}

    td = 0
    uk.sort()
    for i in range(len(uk) - 1):
        for j in range(i + 1, len(uk)):
            if len(uk[j]) < len(uk[i]):
                t = uk[j]
                uk[j] = uk[i]
                uk[i] = t

    for i in range(1, len(uk)):
        j = i
        while j >= 0:
            if uk[i].count(uk[j]) == 0:
                td = 1
            j = j - 1

    if td == 0:
        print('YES')
        for i in uk:
            print(i)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)