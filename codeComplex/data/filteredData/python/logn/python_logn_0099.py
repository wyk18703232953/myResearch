def main(n):
    # 解释输入规模映射：
    # 使用 n 生成一对整数 (a, b)，保证确定性且规模随 n 增长
    # 这里使用简单算术构造：
    #   a = n
    #   b = 2*n + 1
    a = n
    b = 2 * n + 1

    K = 60
    if a == b:
        ans = 0

    else:
        curr = K
        while (b & (1 << curr)) == (a & (1 << curr)):
            curr -= 1
        ans = (1 << curr)
        curr -= 1
        lb = False
        ga = False
        for i in range(curr, -1, -1):
            if (b & (1 << i)) == 0 and (a & (1 << i)) == 0:
                if not lb:
                    ans += (1 << i)
                    ga = True

                else:
                    ans += (1 << i)
            elif (b & (1 << i)) == 0 and (a & (1 << i)) == 1:
                ans += (1 << i)
            elif (b & (1 << i)) == 1 and (a & (1 << i)) == 0:
                if not lb:
                    ans += (1 << i)
                    ga = True
                    lb = True

                else:
                    ans += (1 << i)

            else:
                if not lb:
                    ans += (1 << i)
                    lb = True

                else:
                    ans += (1 << i)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 以做时间复杂度实验
    main(10)