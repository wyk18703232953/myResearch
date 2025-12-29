from collections import Counter
import math
import random

def main(n):
    # 生成测试数据：
    # 原串 l 长度为 n，由'+'和'-'构成
    # 目标串 l1 从 l 中随机改变若干位置（可能为 0）得到
    l = [random.choice(['+', '-']) for _ in range(n)]

    # 随机决定要改变的位置个数 k（0 <= k <= n）
    k = random.randint(0, n)
    change_pos = set(random.sample(range(n), k)) if k > 0 else set()

    l1 = []
    for i, ch in enumerate(l):
        if i in change_pos:
            l1.append('+' if ch == '-' else '-')
        else:
            l1.append(ch)

    # 转为 Counter 统计
    a = Counter(l)
    b = Counter(l1)

    if a['+'] < b['+'] or a['-'] < b['-']:
        print("0")
        return
    else:
        a1 = a['+'] - b['+']
        b1 = a['-'] - b['-']
    s = math.factorial(a1 + b1) // (math.factorial(a1) * math.factorial(b1))
    s1 = float(2 ** (a1 + b1))
    print(s / s1)


# 示例调用
if __name__ == "__main__":
    main(10)