def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def generate_grid(n, offset):
    # 生成 n x n 的字符网格，使用确定性模式
    # 元素在 'a' 到 'z' 之间循环
    return [[chr((i * n + j + offset) % 26 + ord('a')) for j in range(n)] for i in range(n)]

def main(n):
    re = max(1, n)
    # 生成原程序中的 a, b
    a = generate_grid(re, 0)
    # b 为 a 的副本，再做一次确定性的变换，保证逻辑上有结构
    b = [row[:] for row in a]
    # 对 b 做一个与 n 相关但确定性的操作
    # 这里做一次固定的翻转或旋转组合，逻辑上类似“打乱”但完全确定
    if re % 4 == 1:
        b = b[::-1]  # 上下翻转
    elif re % 4 == 2:
        b = [row[::-1] for row in b]  # 左右翻转
    elif re % 4 == 3:
        # 90 度旋转
        c = [['' for _ in range(re)] for _ in range(re)]
        for t in range(re):
            for u in range(re):
                c[t][u] = b[re - u - 1][t]
        b = c

    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = b[::-1]
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = [s[::-1] for s in b]
        c = [['' for _ in range(re)] for _ in range(re)]
        for t in range(re):
            for u in range(re):
                c[t][u] = b[u][re - t - 1]
        b = c[:]
        if check(a, b):
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    main(5)