def fibonacci(limit):
    flist = []
    a, b = 0, 1
    flist.append(a)
    flist.append(b)

    for _ in range(2, limit):
        c = a + b
        a, b = b, c
        flist.append(b)
        if b >= limit:
            break
    return flist


def twopinter(li, i, x):
    z = 0
    # original code used 1-based-like condition i <= len(li)
    # but indexing li[i] requires i < len(li), so we fix it.
    while i < len(li) and (len(li) - z - 1) >= 0 and i <= (len(li) - 1 - z):
        if li[i] + li[len(li) - 1 - z] == x:
            # print(li[i], li[len(li) - 1 - z])
            pass
            return li[i] + li[len(li) - 1 - z]
        elif li[i] + li[len(li) - 1 - z] < x:
            i += 1
        else:  # li[i] + li[len(li)-1-z] > x
            z += 1
    return 0


def threepointer(li, n):
    st = 0
    while st < len(li):
        s = li[st]
        x = n - s
        tp_sum = twopinter(li, st, x)
        if s + tp_sum == n:
            # print(s)
            pass
            # print("Done")
            pass
            return True
        elif s + tp_sum < n:
            st += 1

        else:
            return False
    return False


def main(n):
    # 根据 n 生成测试数据：使用 n 作为上限生成 Fibonacci 数列
    li = fibonacci(n)
    # print(li)
    pass

    if not threepointer(li, n):
        # print("I'm too stupid to solve this problem")
        pass

    # 保留原程序最后一行逻辑
    # print(0, 0, n)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需要修改 n
    main(10)