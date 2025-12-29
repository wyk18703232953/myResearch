import random
import string

def main(n):
    # 1. 生成测试数据：长度为 n 的随机字符串（小写字母）
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：寻找最长重复子串长度
    pb = 0
    lenght = len(s) - 1
    w = []

    while lenght != 0:
        ss = s[pb:pb + lenght]
        w.append(ss)
        if pb + lenght == len(s):
            pb = 0
            lenght -= 1
        else:
            pb += 1

    for i in range(0, len(w) - 1):
        for j in range(i + 1, len(w)):
            if w[i] == w[j]:
                print(len(w[i]))
                return
    print(0)


if __name__ == "__main__":
    # 示例运行：n 可按需修改
    main(10)