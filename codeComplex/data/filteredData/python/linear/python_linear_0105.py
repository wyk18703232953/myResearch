import random
import string

def main(n: int):
    # 生成测试数据：两个长度为 n 的小写字母字符串 s1, s2
    # 若 n <= 0，则默认长度为 1
    length = max(1, n)
    s1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    s2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    # 原始逻辑
    ans = s1[0]
    for i in range(1, len(s1)):
        if s1[i] < s2[0]:
            ans += s1[i]
            if i == len(s1) - 1:
                ans += s2[0]
        else:
            ans += s2[0]
            break
    if len(s1) == 1:
        print(s1[0] + s2[0])
    else:
        print(ans)

if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)