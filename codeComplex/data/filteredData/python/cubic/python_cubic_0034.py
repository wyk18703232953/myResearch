import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机字符串，字符集为小写字母
    S = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    ans = 0
    met = set()

    for i in range(len(S)):
        for j in range(i, -1, -1):
            if S[j:i+1] in met:
                ans = max(ans, i - j + 1)
            else:
                met.add(S[j:i+1])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)