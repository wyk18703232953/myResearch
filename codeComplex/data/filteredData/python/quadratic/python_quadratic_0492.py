import random

def main(n: int):
    # 生成一个满足条件的 d，然后根据 d 反推 a 和 s，再用原逻辑校验
    # 1. 生成一个长度为 n 的随机排列 d（数值范围自定义为 1..n）
    d = list(range(1, n + 1))
    random.shuffle(d)

    # 2. 根据 d 计算 a[i] 和 s[i]
    a = []
    s = []
    for i in range(n):
        left_greater = 0
        right_greater = 0
        for j in range(i):
            if d[j] > d[i]:
                left_greater += 1
        for j in range(i + 1, n):
            if d[j] > d[i]:
                right_greater += 1
        a.append(left_greater)
        s.append(right_greater)

    # 以下为原逻辑（去掉 input），用于校验
    d_check = []
    for q in range(n):
        d_check.append(a[q] + s[q])
    d_check = [n - q for q in d_check]
    for q in range(n):
        f = 0
        for q1 in range(q):
            if d_check[q1] > d_check[q]:
                f += 1
        g = 0
        for q1 in range(q + 1, n):
            if d_check[q1] > d_check[q]:
                g += 1
        if f != a[q] or g != s[q]:
            print('NO')
            break
    else:
        print('YES')
        print(*d_check)


if __name__ == "__main__":
    # 示例：规模为 5，可根据需要修改
    main(5)