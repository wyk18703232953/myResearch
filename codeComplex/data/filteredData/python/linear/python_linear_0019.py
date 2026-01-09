def main(n):
    # n 表示数组长度
    if n <= 0:
        return
    # 确定性构造数组：前 n-1 个为偶数，最后一个为奇数
    # 这样奇数仅有一个，位置在 n，符合原题中“找到不同的那个数”
    s = [2 * i for i in range(n - 1)] + [2 * (n - 1) + 1]

    odd, even, oddIndex, evenIndex = 0, 0, 0, 0
    counter = 0
    for i in s:
        if i % 2 == 0:
            even += 1
            evenIndex = counter

        else:
            odd += 1
            oddIndex = counter
        counter += 1
    ans = evenIndex + 1 if even == 1 else oddIndex + 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)