def main(n):
    # 根据 n 生成测试数据：
    # 这里假设 s 与 n 同阶，设为 n*(n+1)//2，作为一组示例测试数据。
    s = n * (n + 1) // 2

    cnt = 0
    for i in range(n, 0, -1):
        cnt += s // i
        s %= i
    print(cnt)


if __name__ == "__main__":
    # 示例：可修改为任意规模
    main(10)