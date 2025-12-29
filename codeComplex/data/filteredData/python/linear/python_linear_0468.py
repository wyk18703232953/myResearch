import random

def main(n: int) -> int:
    # 1. 生成测试数据：长度为 n，由 'b' 和 'w' 随机组成
    if n <= 0:
        return 0
    chars = ['b', 'w']
    a = ''.join(random.choice(chars) for _ in range(n))

    # 2. 原逻辑
    b = []
    c = 0
    d = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            b.append(['bw'.find(a[c]), i - c])
            d = max(d, i - c)
            c = i
    b.append(['bw'.find(a[c]), n - c])
    d = max(d, n - c)

    if d < n and b[0][0] == (b[-1][0] + b[-1][1]) % 2:
        d = max(d, b[-1][1] + b[0][1])

    print(d)
    return d

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)