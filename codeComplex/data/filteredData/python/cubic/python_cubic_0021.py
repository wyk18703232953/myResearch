import random
import string as pystring

def main(n: int):
    # 1. 生成长度为 n 的随机字符串，字符集为小写字母
    s = ''.join(random.choice(pystring.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：求在所有子串中，重复出现的子串的最大长度
    count1 = []
    longest = 0
    for s_i in range(n):
        for end_i in range(s_i + 1, n + 1):
            sub = s[s_i:end_i]
            if sub not in count1:
                count1.append(sub)
            else:
                if len(sub) > longest:
                    longest = len(sub)

    print(longest)


if __name__ == "__main__":
    # 示例：n 可自行调整
    main(10)