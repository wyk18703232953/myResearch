import random
import string

def main(n: int):
    # 1. 生成规模为 n 的测试数据：随机字符串
    # 可根据需要修改字符集
    chars = string.ascii_lowercase
    S = ''.join(random.choice(chars) for _ in range(n))

    # 2. 原逻辑
    sLen, ans = len(S), 0
    for i in range(sLen):
        for till1 in range(i + 1, sLen):
            till2 = till1 + 1
            for j in range(i + 1, sLen):
                if till2 > sLen:
                    break
                sub1 = S[i:till1]
                sub2 = S[j:till2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                till2 += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可自行修改规模
    main(10)