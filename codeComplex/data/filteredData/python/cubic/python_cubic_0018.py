import random
import string as pystring

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字符串
    s = ''.join(random.choice(pystring.ascii_lowercase) for _ in range(n))
    length = len(s)

    counter = 0
    li = []
    match_li = []

    # 2. 原逻辑
    for i in range(length):
        letter = s[i]
        letters = letter
        if letter in li:
            match_li.append(letter)
        li.append(letter)
        for j in range(i + 1, length):
            letters += s[j]
            if letters in li:
                match_li.append(letters)
            li.append(letters)

    longest = 0
    for k in match_li:
        if len(k) > longest:
            longest = len(k)

    print(longest)


if __name__ == "__main__":
    # 示例：规模 n 可自行调整
    main(10)