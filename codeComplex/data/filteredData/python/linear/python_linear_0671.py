def main(n):
    # 生成确定性输入数组 a，长度为 n
    # 示例构造：a[i] = (i * 2 + 1) // 3，既有奇数也有偶数，且完全由 n 和 i 决定
    a = [(i * 2 + 1) // 3 for i in range(n)]

    b = 0
    for i in range(n):
        if a[i] % 2 == 1:
            if i % 2 == 0:
                b += 1

            else:
                b -= 1

    if n % 2 == 0:
        if b == 0:
            # print("YES")
            pass

        else:
            # print("NO")
            pass

    else:
        if b == 0 or b == 1:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次实验
    main(10)