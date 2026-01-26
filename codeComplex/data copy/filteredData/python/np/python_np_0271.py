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
    # 将 n 映射为原程序的 n 和 q
    # 这里令原始 n = n，q = max(1, n // 2)
    orig_n = max(1, n)
    q = max(1, n // 2)

    root = (orig_n + 1) // 2

    results = []
    for j in range(q):
        # 为第 j 组测试数据生成确定性的 n1 和 str1
        # n1 在 [1, orig_n] 范围内循环
        n1 = (j % orig_n) + 1

        # 操作串长度随 n 增长，这里取 len = max(1, n // 3)
        length = max(1, n // 3)

        # 确定性生成由 'U', 'L', 'R' 组成的字符串
        ops = []
        for i in range(length):
            r = (i + j) % 3
            if r == 0:
                ops.append('U')
            elif r == 1:
                ops.append('L')
            else:
                ops.append('R')
        str1 = ''.join(ops)

        # 原核心逻辑
        for k in range(len(str1)):
            up = find(n1, root)
            if str1[k] == 'U':
                n1 = up
            elif n1 % 2 == 0:
                if str1[k] == 'L':
                    if n1 != root:
                        n1 = (n1 - abs((up - n1) // 2))
                    else:
                        n1 = (n1 - n1 // 2)
                elif str1[k] == 'R':
                    if n1 != root:
                        n1 = (n1 + abs((up - n1) // 2))
                    elif n1 % 2 == 0:
                        n1 = n1 + n1 // 2
        results.append(n1)

    # 为了与原程序行为一致，这里逐行输出每个测试用例的结果
    for ans in results:
        print(ans)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模进行一次实验
    main(10)