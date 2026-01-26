def main(n):
    # 将原来的输入结构 n, a, b 映射为：
    #   n_input = n
    #   a = 1 + (n % 3)        # a ∈ {1,2,3}
    #   b = 1 + ((n // 3) % 3) # b ∈ {1,2,3}
    n_input = max(1, n)  # 保证规模合法且确定
    a = 1 + (n_input % 3)
    b = 1 + ((n_input // 3) % 3)

    n = n_input
    ans = []
    g = {i: set() for i in range(n)}

    if a > 1 and b > 1:
        # print("NO")
        pass
    elif a == 1 and b == 1:
        if n == 1:
            # print("YES")
            pass
            # print("0")
            pass
        elif n < 4:
            # print("NO")
            pass

        else:
            for i in range(n - 1):
                g[i].add(i + 1)
                g[i + 1].add(i)
            for i in range(n):
                tmp = []
                for j in range(n):
                    if i in g[j]:
                        tmp.append('1')

                    else:
                        tmp.append('0')
                ans.append(''.join(tmp))
            # print("YES")
            pass
            # print('\n'.join(ans))
            pass

    else:
        swap = False
        if a == 1:
            a, b = b, a
            swap = True
        for i in range(a - 1, n - 1):
            g[i].add(i + 1)
            g[i + 1].add(i)
        if swap:
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
        # print("YES")
        pass
        # print('\n'.join(ans))
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为规模调用
    main(10)