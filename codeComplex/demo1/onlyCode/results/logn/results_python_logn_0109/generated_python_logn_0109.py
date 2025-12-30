def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里生成 l1 = 0, r = 2^n - 1，保证有一定规模和覆盖位数
    if n <= 0:
        l1, r = 0, 0
    else:
        l1, r = 0, (1 << n) - 1

    if l1 == r:
        print(0)
    else:
        # 注意括号优先级，原表达式 r&(r-1)==0 等价于 (r & (r-1)) == 0
        if (r & (r - 1)) == 0:
            print(r ^ (r - 1))
        else:
            x = l1 ^ r
            p1 = 1
            while p1 <= x:
                p1 *= 2
            print(p1 - 1)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行测试
    main(5)