import random

def x(a, b):
    if a > b:
        return 1
    else:
        return 0

def main(n):
    # 这里的 n 作为规模参数，可用于控制数据范围
    # 生成三对坐标 (a1, a2), (b1, b2), (c1, c2)
    # 坐标值范围根据 n 调整，这里设为 [0, n]
    a1, a2 = random.randint(0, n), random.randint(0, n)
    b1, b2 = random.randint(0, n), random.randint(0, n)
    c1, c2 = random.randint(0, n), random.randint(0, n)

    if (a1 - a2) == (b1 - b2):
        print("NO")
    elif (a1 + a2) == (b1 + b2):
        print("NO")
    elif a1 == b1:
        print("NO")
    elif a2 == b2:
        print("NO")
    elif (a1 - a2) == (c1 - c2):
        print("NO")
    elif (a1 + a2) == (c1 + c2):
        print("NO")
    elif a1 == c1:
        print("NO")
    elif a2 == c2:
        print("NO")
    else:
        if (x(a1, b1) == x(a1, c1)) and (x(a2, b2) == x(a2, c2)):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    # 示例：规模参数为 10
    main(10)