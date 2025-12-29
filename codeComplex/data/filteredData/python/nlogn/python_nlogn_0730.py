import random

def main(n):
    # 生成规模为 n 的测试数据，但算法本身只处理 3 个元素
    # 根据原代码逻辑，每个元素是形如 "1a" 的两字符字符串（数字+字母）
    # 这里先生成 n 个，然后只取前 3 个参与计算，以保持逻辑一致
    cards = []
    for _ in range(n):
        num = random.randint(1, 9)
        suit = random.choice(['a', 'b', 'c', 'd'])
        cards.append(f"{num}{suit}")
    
    # 只取前三个，模拟原始 input().split() 提供的三个字符串
    a = cards[:3]

    a.sort()
    if a[0] == a[1] == a[2]:
        print(0)
        return
    elif a[0] == a[1] or a[1] == a[2]:
        print(1)
        return

    a1 = []
    for i in range(3):
        a1.append([int(a[i][0]), a[i][1]])
    a1.sort()

    if a1[0][1] == a1[1][1] == a1[2][1]:
        if a1[0][0] == a1[1][0] - 1 and a1[0][0] == a1[2][0] - 2:
            print(0)
            return
        for i in range(3):
            for j in range(3):
                if abs(a1[i][0] - a1[j][0]) in (1, 2):
                    print(1)
                    return
        print(2)
        return

    for i in range(3):
        for j in range(i + 1, 3):
            if a1[i][1] == a1[j][1]:
                if a1[i][0] == a1[j][0] - 1 or a1[i][0] == a1[j][0] - 2:
                    print(1)
                else:
                    print(2)
                return
    print(2)


if __name__ == "__main__":
    # 示例调用，n 可以自行修改
    main(10)