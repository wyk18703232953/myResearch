import random

def main(n: int):
    # 1. 生成测试数据：从 'a'~'z' 中随机生成长度为 n 的字符串
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join(random.choice(letters) for _ in range(n))

    # 2. 原逻辑开始（去掉 input()，直接使用生成的 s）
    s2 = s + s
    length = len(s2)
    an = 1
    m = 1

    for i in range(1, length):
        if s2[i] != s2[i - 1]:
            m += 1
            an = max(an, m)
        else:
            an = max(an, m)
            m = 1

    result = min(an, length // 2)

    # 为了方便验证，可以打印原串和结果，如果只需结果可只打印 result
    print("s:", s)
    print("answer:", result)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)