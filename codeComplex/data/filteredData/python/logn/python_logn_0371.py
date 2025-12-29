M = 1000000007

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设定：
    # x = n, k = n
    x = n
    k = n

    if x == 0:
        print(0)
    else:
        ans = ((pow(2, k + 1, M) * x) % M - pow(2, k, M) + 1) % M
        print(ans)


if __name__ == "__main__":
    # 示例：可以在此处调用 main 进行测试
    main(10)