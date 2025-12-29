def main(n):
    # 根据规模 n 生成一组 (n, s) 测试数据
    # 这里简单设定 s = n // 2，可按需要调整生成策略
    s = n // 2

    def check(x):
        return x - sum(int(d) for d in str(x)) >= s

    if n - sum(int(d) for d in str(n)) < s:
        ans = 0
    else:
        start, end = 1, n
        mid = (start + end) // 2
        while mid != end and mid != start:
            if check(mid):
                end = mid
            else:
                start = mid
            mid = (start + end) // 2
        ans = n - end + 1

    print(ans)


# 示例：调用 main(100) 运行
if __name__ == "__main__":
    main(100)