import sys
import random

def main(n):
    # 生成测试数据：随机选择 k，保证 n*k 有一定规模
    if n <= 0:
        return
    k = random.randint(1, max(1, n))

    ans = []
    total = n * k
    for i in range(1, total + 1):
        if i % 2:
            x, y = divmod(i // 2, k)
            ans.append([x + 1, y + 1])
        else:
            x, y = divmod(total - i // 2, k)
            ans.append([x + 1, y + 1])

    out = sys.stdout.write
    for a, b in ans:
        out(f"{a} {b}\n")


if __name__ == "__main__":
    # 示例：可在此处调整 n 的大小做简单测试
    main(5)