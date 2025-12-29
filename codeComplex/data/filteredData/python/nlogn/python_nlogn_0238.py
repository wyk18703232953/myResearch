import random

def scal(x1, y1, x2, y2, x3, y3):
    # 判断三点是否共线
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0

def check(lst, n, s1, s2):
    for x in range(n - 2):
        if len(s2) >= 3:
            if not scal(lst[s2[-3]][0], lst[s2[-3]][1],
                       lst[s2[-2]][0], lst[s2[-2]][1],
                       lst[s2[-1]][0], lst[s2[-1]][1]):
                return False
        if scal(lst[0][0], lst[0][1],
                lst[1][0], lst[1][1],
                lst[x + 2][0], lst[x + 2][1]):
            s1.append(x + 2)
        else:
            s2.append(x + 2)
    if len(s2) >= 3:
        if not scal(lst[s2[-3]][0], lst[s2[-3]][1],
                   lst[s2[-2]][0], lst[s2[-2]][1],
                   lst[s2[-1]][0], lst[s2[-1]][1]):
            return False
    return True

def generate_test_data(n):
    # 生成 n 个点 (a, b)，坐标范围可按需调整
    # 为避免所有点共线，做一个简单处理：
    pts = []
    for i in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        pts.append((x, y))
    return pts

def main(n):
    # 生成测试数据
    lst = generate_test_data(n)

    flag = True

    if n >= 5:
        # 三个列表在 check 中被修改，因此每次调用前重置
        s1 = []
        s2 = []
        if not check(lst, n, s1, s2):
            lst[1], lst[s2[0]] = lst[s2[0]], lst[1]
            x = s2[0]  # 和原代码一致，即便 x 未再使用
            s1 = []
            s2 = []
            if not check(lst, n, s1, s2):
                lst[0], lst[s2[0]] = lst[s2[0]], lst[0]
                s1 = []
                s2 = []
                if not check(lst, n, s1, s2):
                    flag = False

    if flag:
        print("YES")
    else:
        print("NO")


# 示例：直接运行本文件时，给定一个 n 调用 main
if __name__ == "__main__":
    main(10)