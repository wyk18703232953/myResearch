def main(n):
    # 生成测试数据：根据 n 构造一组 (a, b)
    # 这里简单设定：若 n 很小则用 a=b=1，否则用 a=1, b=2 做一组可行数据
    if n == 1:
        a, b = 1, 1
    elif n < 4:
        a, b = 1, 1
    else:
        a, b = 1, 2

    ans = []
    g = {i: set() for i in range(n)}

    if a > 1 and b > 1:
        print("NO")
    elif a == 1 and b == 1:
        if n == 1:
            print("YES")
            print("0")
        elif n < 4:
            print("NO")
        else:
            # 构造路径图
            for i in range(n - 1):
                g[i].add(i + 1)
                g[i + 1].add(i)
            # 输出邻接矩阵
            for i in range(n):
                tmp = []
                for j in range(n):
                    if i in g[j]:
                        tmp.append('1')
                    else:
                        tmp.append('0')
                ans.append(''.join(tmp))
            print("YES")
            print('\n'.join(ans))
    else:
        swap = False
        if a == 1:
            a, b = b, a
            swap = True
        # 从 a-1 开始构造一条链
        for i in range(a - 1, n - 1):
            g[i].add(i + 1)
            g[i + 1].add(i)
        if swap:
            # 取补图（去掉自环）
            for i in range(n):
                tmp = []
                for j in range(n):
                    if i == j:
                        tmp.append('0')
                    elif i not in g[j]:
                        tmp.append('1')
                    else:
                        tmp.append('0')
                ans.append(''.join(tmp))
        else:
            for i in range(n):
                tmp = []
                for j in range(n):
                    if i in g[j]:
                        tmp.append('1')
                    else:
                        tmp.append('0')
                ans.append(''.join(tmp))
        print("YES")
        print('\n'.join(ans))


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(5)