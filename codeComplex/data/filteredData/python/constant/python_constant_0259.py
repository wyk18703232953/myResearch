import math
import random

def main(n):
    # 生成测试数据：保证 1 <= l <= r <= n, 1 <= pos <= n
    # 这里随机生成一组 (pos, l, r)，你可以按需要替换为确定性生成
    l = random.randint(1, n)
    r = random.randint(l, n)
    pos = random.randint(1, n)

    # 原逻辑
    if l == 1 and r == n:
        ans = 0
    elif l == 1:
        if pos == r:
            ans = 1
        elif pos > r:
            ans = pos - r + 1
        else:  # pos < r
            ans = r - pos + 1
    elif r == n:
        if pos == l:
            ans = 1
        elif pos < l:
            ans = l - pos + 1
        else:
            ans = pos - l + 1
    else:
        if l <= pos <= r:
            if pos - l < r - pos:
                ans = 2 + pos - l + r - l
            else:
                ans = 2 + r - l + r - pos
        else:
            if pos > r:
                ans = pos - r + 2 + r - l
            else:
                ans = l - pos + 2 + r - l

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 可根据需要修改
    main(10)