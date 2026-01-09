def main(n):
    li = []
    for i in range(1, n + 1):
        if n % i == 0:
            li.append(i)
    p = 0
    for t in li:
        l = [m for m in str(t)]
        if set(l) == {'4'} or set(l) == {'7'} or set(l) == {'4', '7'}:
            p += 1
    if p > 0:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例：以 n 的大小作为输入规模，本例使用 n = 100000 作为演示
    main(100000)