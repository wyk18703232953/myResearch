def main(n: int):
    # 生成类似原始代码中 details 的“幸运数”列表，规模随 n 增长
    # 原始列表：4, 7, 44, 77, 444, 777, 47, 74, 447, 774, 474, 747, 477
    # 这里按“只包含4和7的数”规则生成所有 <= n 的幸运数
    details = []

    def generate_lucky_numbers(current: int):
        if current > n:
            return
        if current != 0:
            details.append(current)
        generate_lucky_numbers(current * 10 + 4)
        generate_lucky_numbers(current * 10 + 7)

    generate_lucky_numbers(0)

    f = 0
    for i in details:
        if i != 0 and n % i == 0:
            f = 1
            break

    if f:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：根据 n 的规模进行测试，这里给一个示例 n
    # 实际使用时，可在外部调用 main(任意整数 n)
    test_n = 1000
    main(test_n)