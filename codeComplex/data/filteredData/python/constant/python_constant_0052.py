import random

def main(n: int):
    c = 0
    lst = [4, 7, 47, 74, 447, 474, 744, 477, 747, 774]
    if n in lst:
        print("YES")
    else:
        for i in lst:
            if n % i == 0:
                print("YES")
                c += 1
                break
        if c == 0:
            print("NO")


if __name__ == "__main__":
    # 根据规模 n 生成测试数据，这里示例为在 [1, 10^n] 范围内随机生成一个整数
    n_scale = 3  # 可修改规模
    test_n = random.randint(1, 10 ** n_scale)
    main(test_n)