def main(n):
    # n 表示数组长度
    # 生成一个确定性的数组 a，元素为 i % 10
    a = [i % 10 for i in range(n)]
    b = sorted(a)
    op = 0
    for i in range(n):
        if a[i] == b[i]:
            continue
        op += 1
    if op == 0 or op == 2:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)