def main(n):
    # 生成确定性的字符串 a 和 b，长度为 n
    # a: 循环 "ab"
    # b: 循环 "ba"
    a = ''.join('a' if i % 2 == 0 else 'b' for i in range(n))
    b = ''.join('b' if i % 2 == 0 else 'a' for i in range(n))

    k = True
    result = 0
    z = None  # 为了保持变量作用域与原逻辑一致，初始化 z

    for i in range(n):
        if a[i] == b[i]:
            if k is False:
                result += 1
            k = True

        else:
            if k is False and z != a[i]:
                result += 1
                k = True
            elif k is False and z == a[i]:
                result += 1

            else:
                k = False
                z = a[i]
    if k is False:
        result += 1

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次运行
    main(10)