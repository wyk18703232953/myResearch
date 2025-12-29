import random
import string

def main(n: int):
    # 1. 根据规模 n 生成测试字符串：由小写字母随机组成
    #    这里生成长度为 n 的字符串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    ans = 0
    sLen = len(s)

    # 2. 原始逻辑：穷举两个子串并比较
    for i in range(sLen):
        for till1 in range(i + 1, sLen + 1):
            till2 = till1 + 1
            for j in range(i + 1, sLen + 1):
                if till2 > sLen:
                    break
                sub1 = s[i:till1]
                sub2 = s[j:till2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                till2 += 1

    print(ans)


if __name__ == "__main__":
    # 示例：可修改这里的 n 来调整规模
    main(10)