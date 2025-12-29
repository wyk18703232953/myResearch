import random
import string


def main(n: int):
    # 1. 生成长度为 n 的随机小写字母字符串作为 name
    # 可按需要修改字符集或生成策略
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for _ in range(n))

    # 2. 原逻辑：找最长重复子串的长度并输出
    for i in range(len(name), 0, -1):
        for j in range(len(name) - i + 1):
            if name[j: j + i] in name[j + 1:]:
                print(i)
                return
    print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)