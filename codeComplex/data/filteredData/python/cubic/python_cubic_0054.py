import random
import string

def main(n: int):
    # 1. 生成规模为 n 的测试数据：随机小写字符串
    #    可根据需要修改字符集
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    sLen, ans = len(s), 0

    for i in range(sLen - 1):
        for till1 in range(i + 1, sLen):
            till2 = till1 + 1
            for j in range(i + 1, sLen):
                if till2 > sLen:
                    break
                sub1 = s[i:till1]
                sub2 = s[j:till2]
                subLen = len(sub1)
                if sub1 == sub2 and subLen > ans:
                    ans = subLen
                till2 += 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10 的测试
    main(10)