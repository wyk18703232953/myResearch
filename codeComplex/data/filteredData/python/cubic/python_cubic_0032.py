import random
import string

def main(n: int):
    # 1. 根据 n 生成测试数据：随机字符串，长度为 n
    # 可以根据需要调整字符集
    chars = string.ascii_lowercase
    inputS = ''.join(random.choice(chars) for _ in range(n))

    ans = 0
    # 2. 原逻辑：求最长重复子串长度
    for i in range(0, len(inputS) - 1):
        for count in range(1, len(inputS)):
            for j in range(i + 1, len(inputS) - count + 1):
                A = inputS[i: i + count]
                B = inputS[j: j + count]
                if A == B:
                    ans = count if count > ans else ans

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)