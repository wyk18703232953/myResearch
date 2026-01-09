x = None
y = None
z = None
t1 = None
t2 = None
t3 = None

def main(n):
    global x, y, z, t1, t2, t3
    # 根据 n 确定性生成输入数据
    # 让 x, y, z 成为与 n 线性相关的不同值
    x = n
    y = 2 * n
    z = 3 * n
    # 时间系数也随 n 变化，但保持简单线性关系
    t1 = n + 1
    t2 = n + 2
    t3 = (n // 2) + 1

    time1 = abs(x - y) * t1
    time2 = (abs(x - y) + abs(z - x)) * t2 + 3 * t3
    if time2 <= time1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)