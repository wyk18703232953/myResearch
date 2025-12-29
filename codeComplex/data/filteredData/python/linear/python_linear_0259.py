import random
import string

def main(n: int):
    # 生成长度为 n 的随机小写字母串作为测试数据
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    n_len = len(s)
    Ans = 0
    for i in range(n_len):
        for j in range(i + 1, n_len):
            L = i
            R = j
            while L < R and s[L] == s[R]:
                L += 1
                R -= 1
            if L < R and Ans < j - i + 1:
                Ans = j - i + 1
    print(Ans)

# 示例：需要时可调用 main(n)
# main(10)