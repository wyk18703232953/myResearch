def main(n):
    # 映射：原程序中 n = 规模参数，v 作为 n 的函数确定生成
    # 保持相对规模线性：设 v = n 的平方
    v = n * n

    b = 0
    ans = 0
    sss = 0
    for i in range(1, n + 1):
        while b < v:
            if sss == n - 1:
                break
            sss += 1
            ans += i
            b += 1
        b -= 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)