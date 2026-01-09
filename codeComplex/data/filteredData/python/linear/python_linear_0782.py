def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成输入数据：模 3 的重复结构，保证存在重复元素和多样性
    a = [(i // 2) % (max(1, n // 3)) for i in range(n)]

    # 对应原代码逻辑
    a.sort()
    cnt = 0
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            a[i] -= 1
            cnt += 1
            break
    if a[0] < 0:
        # print('cslnb')
        pass
        return

    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            # print('cslnb')
            pass
            return

    for i, x in enumerate(a):
        cnt += x - i

    # print('sjfnb' if (cnt & 1) else 'cslnb')
    pass
if __name__ == "__main__":
    main(10)