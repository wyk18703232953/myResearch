import random

def main(n: int):
    # 生成测试数据：根据规模 n 构造一个合适的 m
    # 这里示例：m 在 [1, 3] 范围内随机取值
    m = random.randint(1, 3)

    a = []
    b = []
    check = True
    tmp_n = n  # 避免修改传入参数

    while tmp_n >= 0:
        if check:
            a.append(5)
            tmp_n -= 5
            b.append(4)
            check = False
        else:
            check = True
            a.append(4)
            tmp_n -= 4
            b.append(5)

    if m != 1:
        a.append(5)
        b.append(6)
    else:
        a.append(5)
        b.append(5)

    print(*a, sep="")
    print(*b, sep="")


if __name__ == "__main__":
    # 示例：调用 main(20) 进行测试
    main(20)