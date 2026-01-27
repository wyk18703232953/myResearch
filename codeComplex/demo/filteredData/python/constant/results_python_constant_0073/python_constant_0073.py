ser = [0, 1]

def fib(n):
    global ser
    ser = [0, 1]  # 重置序列，避免多次调用 main 时受上次影响
    i = 1
    while i < n:
        ser.append(i)
        i = ser[-1] + ser[-2]
    if i != n:
        return -1

    else:
        return len(ser)

def main(n):
    a, b, c = 0, 0, 0
    ans = 1
    if n == 0:
        ans = 1
    elif n == 1:
        a = 1
    elif n == 2:
        a = 1
        b = 1
    elif n == 3:
        a = 1
        b = 1
        c = 1

    else:
        ans = fib(n)
        if ans != -1:
            a = ser[ans-2]
            b = ser[ans-2]
            c = ser[ans-3]
    if ans != -1:
        # print(a, b, c)
        pass

    else:
        # print("I'm too stupid to solve this problem")
        pass
if __name__ == "__main__":
    # 根据 n 生成测试数据，这里直接给一个示例 n
    test_n = 21
    main(test_n)