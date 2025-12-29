import random

def main(n):
    # n 用于控制测试数据规模，这里用来影响数字范围和随机性
    max_digit = max(1, min(8, n))  # 数字 1~max_digit
    letters = 'abcd'               # 限制在少量字母便于测试
    # 生成格式为 "d1c1 d2c2 d3c3" 的字符串，其中 di 为数字字符，ci 为字母
    parts = []
    for _ in range(3):
        d = str(random.randint(1, max_digit))
        c = random.choice(letters)
        parts.append(d + c)
    s = ' '.join(parts)

    s1 = s[0:2]
    s2 = s[3:5]
    s3 = s[6:8]

    def func(inp):
        ans = 2
        num = int(inp[0])
        c = inp[1]
        ans = min(ans, 2 - int(s.find(str(num + 1) + c) != -1) - int(s.find(str(num + 2) + c) != -1))
        ans = min(ans, 2 - int(s.find(str(num + 1) + c) != -1) - int(s.find(str(num - 1) + c) != -1))
        ans = min(ans, 2 - int(s.find(str(num - 1) + c) != -1) - int(s.find(str(num - 2) + c) != -1))
        ans = min(ans, 3 - s.count(inp))
        return ans

    ans = 2
    ans = min(ans, func(s1))
    ans = min(ans, func(s2))
    ans = min(ans, func(s3))

    print(s)    # 若只想保留原逻辑输出，可注释掉这一行
    print(ans)


if __name__ == "__main__":
    main(10)