def main(n):
    # 这里根据 n 生成测试数据：k 可以根据某种规则生成
    # 示例：令 k = n*(n+3)//2 - n，保证存在整数解 x = n
    # 因为 x(x+3) = 2(k+n)，若令 x = n，则
    # n(n+3) = 2(k+n) => k = (n(n+3) - 2n) / 2 = n(n+1)/2
    k = n * (n + 1) // 2

    ans = None
    for x in range(1, n + 1):
        if x * (x + 3) == 2 * (k + n):
            ans = n - x
            break
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(10)