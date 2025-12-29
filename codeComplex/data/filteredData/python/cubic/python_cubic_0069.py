import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机字符串，字符集用小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    slen = len(s)
    ans = 0
    for st1 in range(slen - 1):
        for end1 in range(st1 + 1, slen):
            end2 = end1 + 1
            sub1 = s[st1:end1]
            for st2 in range(st1 + 1, slen):
                if end2 > slen:
                    break

                sub2 = s[st2:end2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                end2 += 1

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)