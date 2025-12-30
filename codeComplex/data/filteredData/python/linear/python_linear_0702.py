import random

def main(n: int):
    # 生成长度为 n 的随机操作序列，元素为 '+' 或 '-'
    ops = ''.join(random.choice(['+', '-']) for _ in range(n))

    b = 0
    for ch in ops:
        if ch == '+':
            b += 1
        else:
            b -= 1
            b = max(b, 0)

    print(b)

# 示例调用：
# main(10)