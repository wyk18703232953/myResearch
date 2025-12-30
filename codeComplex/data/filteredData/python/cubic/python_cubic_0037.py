import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机字符串，字符集为小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：求字符串中出现至少两次的最长子串长度
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if s[j: j + i] in s[j + 1:]:
                print(i)
                return
    print(0)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行测试
    main(10)