import random

def main(n: int):
    # 生成长度为 n 的随机字符串，字符为 '+' 或 '-'
    s = ''.join(random.choice('+-') for _ in range(n))

    cur = 0
    for a in s:
        cur = max(cur, 0)
        if a == '-':
            cur -= 1
        else:
            cur += 1
        cur = max(cur, 0)
    print(cur)

# 示例：需要时可调用 main(n)
# main(10)