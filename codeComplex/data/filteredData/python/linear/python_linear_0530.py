import random
import string

def main(n):
    # 随机生成参数 k，1 <= k <= 26，且 k <= n
    k = random.randint(1, min(26, n))

    # 随机生成长度为 n 的由大写字母组成的字符串 s
    s = ''.join(random.choice(string.ascii_uppercase) for _ in range(n))

    # 原逻辑
    ct = [0] * 26
    for ch in s:
        ct[ord(ch) - ord('A')] += 1

    result = min(ct[:k]) * k
    print(result)

if __name__ == "__main__":
    # 示例：可根据需要修改 n 的取值或从外部调用 main(n)
    main(100)