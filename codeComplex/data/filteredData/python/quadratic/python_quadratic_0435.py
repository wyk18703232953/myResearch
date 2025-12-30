import math
import random

def main(n: int):
    # 生成测试数据：长度为 n 的仅含 '0'~'9' 的字符串
    # 为了尽量覆盖逻辑，这里随机生成，但保证至少有一个非零数字（除非 n==0）
    if n <= 0:
        s2 = ""
    else:
        # 随机决定是否全部为 '0'（可以覆盖 len(s)==0 的分支）
        if random.random() < 0.3:
            s2 = "0" * n
        else:
            chars = []
            for i in range(n):
                # 生成 0~9 的随机数字
                d = random.randint(0, 9)
                chars.append(str(d))
            # 确保不是全 0（如果需要）
            if all(ch == '0' for ch in chars):
                chars[random.randrange(n)] = str(random.randint(1, 9))
            s2 = "".join(chars)

    # 以下逻辑与原代码等价，只是去掉了 input()
    s2 = list(s2)
    s = []
    for i in range(len(s2)):
        if s2[i] == '0':
            continue
        else:
            s.append(int(s2[i]))
    s1 = sum(s)
    n = len(s)
    l = []
    for i in range(2, n + 1):
        if s1 % i == 0:
            l.append(s1 // i)
    f = 0
    if len(s) == 0:
        f = 1
    for i in range(len(l)):
        c = 0
        if f == 1:
            break
        for j in range(n):
            c += s[j]
            if c == l[i]:
                c = 0
                if j == n - 1:
                    f = 1
            elif c < l[i]:
                c = c
            else:
                break
    if f == 0:
        print('NO')
    else:
        print('YES')

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)