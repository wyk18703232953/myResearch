def main(n):
    dict1 = {}
    dict2 = {}
    # 生成确定性输入数据：n 行形如 "(a+b)/c" 的表达式
    # 设 a=i, b=i+1, c=(i%5)+1，避免除以 0
    for i in range(n):
        a = i
        b = i + 1
        c = (i % 5) + 1
        ans = (a + b) / c
        if ans in dict2:
            dict2[ans] += 1

        else:
            dict2[ans] = 1
        dict1[i] = ans
    for i in range(n):
        # print(dict2[dict1[i]], end=' ')
        pass
if __name__ == "__main__":
    main(10)