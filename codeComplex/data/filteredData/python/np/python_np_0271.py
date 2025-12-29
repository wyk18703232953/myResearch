import random

def find(x, root):
    if root == x:
        u = root
    else:
        i = 0
        s = 2 ** i
        while x % s == 0:
            i += 1
            s = 2 ** i
        s = s // 2
        y = i + 1
        if (x - s) % (2 ** y) != 0:
            u = x - s
        else:
            u = x + s
    return u

def main(n):
    # 规模 n：树大小为 n，根为 (n+1)//2
    root = (n + 1) // 2

    # 生成测试数据：随机生成 q 组查询
    # 这里令 q = max(1, n // 10) 作为示例，可根据需要调整
    q = max(1, n // 10)

    for _ in range(q):
        # 随机生成起点 n1：1..n
        n1 = random.randint(1, n)

        # 随机生成操作串：长度在 1..min(2*n, 50) 之间
        # 字符来自 'U', 'L', 'R'
        str_len = random.randint(1, min(2 * n, 50))
        ops = ['U', 'L', 'R']
        str1 = ''.join(random.choice(ops) for _ in range(str_len))

        cur = n1
        for ch in str1:
            up = find(cur, root)
            if ch == 'U':
                cur = up
            elif cur % 2 == 0:
                if ch == 'L':
                    if cur != root:
                        cur = cur - abs((up - cur) // 2)
                    else:
                        cur = cur - cur // 2
                elif ch == 'R':
                    if cur != root:
                        cur = cur + abs((up - cur) // 2)
                    elif cur % 2 == 0:
                        cur = cur + cur // 2

        print(cur)

if __name__ == "__main__":
    # 示例调用：n = 15
    main(15)