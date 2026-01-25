from collections import deque

def main(n):
    # 生成确定性输入：n 表示序列长度，m 取等于 n，k 取固定值
    m = n
    k = 5 if n > 0 else 1
    # 生成严格递增且分布在若干页中的序列
    a = deque([(i * 3) % (n * 3 + 7) + 1 for i in range(n)])
    a = deque(sorted(a))

    oper = 0
    rem = 0
    while a:
        x = a.popleft()
        pg = (x - 1 - rem) // k
        lrem = 1
        while a and (a[0] - 1 - rem) // k == pg:
            a.popleft()
            lrem += 1
        rem += lrem
        oper += 1
    print(oper)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)