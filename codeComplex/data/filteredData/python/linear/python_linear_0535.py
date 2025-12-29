import random
import string

def main(n):
    # 随机生成 k（字母种类数），1 <= k <= min(26, n)
    if n <= 0:
        return 0

    k = random.randint(1, min(26, n))

    # 使用前 k 个大写字母生成长度为 n 的随机字符串
    letters = string.ascii_uppercase[:k]
    s = [random.choice(letters) for _ in range(n)]

    a = ord('A')
    cnt = [0] * k
    for ch in s:
        cnt[ord(ch) - a] += 1

    result = k * min(cnt)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)