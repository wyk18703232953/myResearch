def main(n):
    # 映射：原程序中 n 为规模，v 为与 n 同阶的规模参数
    # 这里令 v = n，使规模含义清晰且可控
    v = n
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
    # 示例：可根据需要修改 n 进行实验
    main(10)