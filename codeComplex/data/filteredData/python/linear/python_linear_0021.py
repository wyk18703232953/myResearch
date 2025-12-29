import random

def judge(x):
    return 0 if x % 2 == 0 else 1

def main(n):
    # 生成测试数据：长度为 n 的整数列表
    # 为保证逻辑有意义，构造“多数奇/偶 + 少数1个相反奇/偶”的数据
    if n < 3:
        raise ValueError("n 必须 >= 3")

    # 随机决定多数是偶数还是奇数
    majority_parity = random.choice([0, 1])  # 0: 偶, 1: 奇
    minority_parity = 1 - majority_parity

    # 随机选择“异类”的位置
    minority_pos = random.randint(0, n - 1)

    ls = []
    for i in range(n):
        if i == minority_pos:
            # 生成与多数不同奇偶性的数
            if minority_parity == 0:  # 需要偶数
                x = random.randrange(0, 1000, 2)
            else:  # 需要奇数
                x = random.randrange(1, 1000, 2)
        else:
            # 生成与多数相同奇偶性的数
            if majority_parity == 0:  # 偶数
                x = random.randrange(0, 1000, 2)
            else:  # 奇数
                x = random.randrange(1, 1000, 2)
        ls.append(x)

    # 按原逻辑寻找异类的下标（1-based）
    if judge(ls[0]) == judge(ls[1]):
        for x in ls[2:]:
            if judge(x) != judge(ls[0]):
                print(ls.index(x) + 1)
                break
    else:
        if judge(ls[2]) == judge(ls[0]):
            print(2)
        elif judge(ls[2]) == judge(ls[1]):
            print(1)

    return ls  # 如需查看生成的数据，可使用返回值

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)