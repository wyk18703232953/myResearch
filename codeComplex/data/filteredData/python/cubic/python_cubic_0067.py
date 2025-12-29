import random
import string

def main(n: int):
    # 生成长度为 n 的随机小写字母串
    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for _ in range(n))

    # 原逻辑开始
    for _ in range(1):
        for l in range(len(s), 0, -1):
            k = []
            for i in range(0, len(s) - l + 1):
                k.append(s[i:i + l])
            if len(k) != len(list(set(k))):
                print(l)
                return
        print(0)


if __name__ == "__main__":
    # 示例：规模 n = 10，可根据需要修改
    main(10)