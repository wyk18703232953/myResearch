from math import factorial

def main(n):
    # 生成确定性的 word1 和 word2，长度都与 n 相关
    # 使用 '++-+' 的周期模式构造，避免随机性
    pattern = ['+', '+', '-', '+']
    len1 = max(1, n)          # 保证至少长度为 1
    len2 = max(1, n + 1)      # 为了产生不同的 expected/blank 组合

    word1 = [pattern[i % 4] for i in range(len1)]

    # 对于 word2，使用 '+-?' 的周期模式，其中 '?' 代表空位
    pattern2 = ['+', '-', '?']
    raw2 = [pattern2[i % 3] for i in range(len2)]
    # 将 '?' 转成原题中的未知字符（这里用 '?'，与原逻辑中“else”分支对应）
    word2 = raw2

    expected = 0
    for i in word1:
        if i == '+':
            expected += 1
        else:
            expected -= 1

    blank = 0
    for i in word2:
        if i == '+':
            expected -= 1
        elif i == '-':
            expected += 1
        else:
            blank += 1

    if abs(expected) > blank:
        print(float(0))
    elif blank == 0:
        if expected == 0:
            print(1)
        else:
            print(0)
    else:
        total = 2 ** blank
        if expected == blank - 1:
            print(float(0))
        else:
            f = (blank - expected) // 2
            if expected > 0:
                a, b = expected + f, f
            elif expected < 0:
                a, b = expected + f, f
            else:
                a, b = f, f
            ans = factorial(a + b) / factorial(a)
            ans = ans / factorial(b)
            ans = ans / total
            print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)