def main(n):
    # 生成测试数据：这里将 k 设置为 n，可按需要修改为其他生成方式
    k = n

    x = [0, 9]
    i = 2
    y = 90
    while x[-1] < 10**12:
        x.append(x[-1] + y * i)
        y *= 10
        i += 1

    if k in x:
        # print(9)
        pass

    else:
        for t in range(len(x)):
            if k < x[t]:
                break
        e = k - x[t - 1]
        if t == 1:
            q = str(e)

        else:
            q = str(10**(t - 1) + e // t - 1)
        if e % t == 0:
            # print(q[-1])
            pass

        else:
            q = str(int(q) + 1)
            # print(q[e % t - 1])
            pass
if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)