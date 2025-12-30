import random
import string

def solve_from_strings(s):
    b = []
    b.append((s[0][1], int(s[0][0])))
    b.append((s[1][1], int(s[1][0])))
    b.append((s[2][1], int(s[2][0])))
    b.sort()
    if (b[0][0] == b[1][0] and b[1][0] == b[2][0]):
        if (b[0] == b[1] and b[1] == b[2]):
            return 0
        elif (b[0][1] + 1 == b[1][1] and b[1][1] + 1 == b[2][1]):
            return 0
        elif (b[0] == b[1]):
            return 1
        elif (b[1] == b[2]):
            return 1
        elif b[0][1] + 1 == b[1][1]:
            return 1
        elif b[0][1] + 2 == b[1][1]:
            return 1
        elif b[1][1] + 1 == b[2][1]:
            return 1
        elif b[1][1] + 2 == b[2][1]:
            return 1
        elif b[0][1] + 1 == b[2][1]:
            return 1
        elif b[0][1] + 2 == b[2][1]:
            return 1
        else:
            return 2
    elif (b[0][0] != b[1][0] and b[1][0] != b[2][0] and b[2][0] != b[0][0]):
        return 2
    elif b[0][0] == b[1][0]:
        if b[0] == b[1]:
            return 1
        elif b[0][1] + 1 == b[1][1]:
            return 1
        elif b[0][1] + 2 == b[1][1]:
            return 1
        else:
            return 2
    elif b[1][0] == b[2][0]:
        if (b[1] == b[2]):
            return 1
        elif b[1][1] + 1 == b[2][1]:
            return 1
        elif b[1][1] + 2 == b[2][1]:
            return 1
        else:
            return 2
    else:
        return 2

def generate_test_data(n):
    # 生成 n 组三张牌，每张牌格式如 "1a"（数字+字母）
    data = []
    for _ in range(n):
        nums = [str(random.randint(1, 9)) for _ in range(3)]
        suits = [random.choice(string.ascii_lowercase) for _ in range(3)]
        three_cards = [nums[i] + suits[i] for i in range(3)]
        data.append(three_cards)
    return data

def main(n):
    tests = generate_test_data(n)
    for s in tests:
        ans = solve_from_strings(s)
        print("Input:", " ".join(s), " Output:", ans)

if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)