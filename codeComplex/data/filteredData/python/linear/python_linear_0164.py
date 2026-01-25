def main(n):
    dict1 = {}
    dict2 = {}

    # 生成确定性的测试数据，模拟原来的输入格式 "(a+b)/c"
    # 这里将 n 映射为表达式数量
    for i in range(n):
        a = i
        b = i // 2 + 1
        c = (i % 5) + 1
        ans = (a + b) / c
        if ans in dict2:
            dict2[ans] += 1
        else:
            dict2[ans] = 1
        dict1[i] = ans

    for i in range(n):
        print(dict2[dict1[i]], end=' ')


if __name__ == "__main__":
    main(10)