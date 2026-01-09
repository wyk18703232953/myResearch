def main(n):
    m = 1000000007

    # 生成测试数据：根据 n 生成 x, k
    # 可根据需求修改生成逻辑，这里简单设定：
    x = n
    k = n

    up = (x * pow(2, k + 1, m)) % m
    down = pow(2, k, m) - 1
    if x == 0:
        # print(0)
        pass

    else:
        # print((up - down) % m)
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)