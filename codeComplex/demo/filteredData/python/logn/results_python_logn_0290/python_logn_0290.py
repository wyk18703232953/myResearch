def main(n: int):
    """
    依据规模 n 生成测试数据：
    - x = n
    - k = n // 2
    并输出原程序对应结果
    """
    mo = 1000000007
    x = n
    k = n // 2

    if not x:
        # print(0)
        pass
    elif not k:
        # print((x * 2) % mo)
        pass

    else:
        ans = x * pow(2, k + 1, mo) + 1 - pow(2, k, mo)
        ans %= mo
        ans += mo
        ans %= mo
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值进行测试
    main(10)