import random

def main(n):
    # 随机生成初始的 s（题意中为一个下界或初始值）
    s = random.randint(0, 100)

    mins = s
    mylist = []

    # 根据 n 生成测试数据并计算 person + floor
    for _ in range(n):
        # 这里假设 person 和 floor 的取值范围为 [0, 100]
        person = random.randint(0, 100)
        floor = random.randint(0, 100)
        mylist.append(person + floor)

    val = max(mylist) if mylist else mins

    if val < mins:
        print(mins)
    else:
        print(val)


if __name__ == "__main__":
    # 示例：调用 main(5)，规模为 5
    main(5)