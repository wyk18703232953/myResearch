import random

def main(n: int):
    # 生成一组符合题意的构造（从随机排列构造 le, ri，再用原逻辑验证）
    # 1. 随机生成一个排列 check
    check = list(range(1, n + 1))
    random.shuffle(check)

    # 2. 根据 check 生成 le, ri
    le = [0] * n
    ri = [0] * n
    for i in range(n):
        cnt_left = 0
        for j in range(i - 1, -1, -1):
            if check[j] > check[i]:
                cnt_left += 1
        le[i] = cnt_left

    for i in range(n):
        cnt_right = 0
        for j in range(i + 1, n):
            if check[j] > check[i]:
                cnt_right += 1
        ri[i] = cnt_right

    # 3. 用原始逻辑验证 le, ri 是否可行
    notp = False
    rebuilt = []
    for i in range(n):
        rebuilt.append(n - le[i] - ri[i])

    for i in range(n):
        tot = 0
        for j in range(i - 1, -1, -1):
            if rebuilt[j] > rebuilt[i]:
                tot += 1
        if tot != le[i]:
            notp = True
            break

    if not notp:
        for i in range(n):
            tot = 0
            for j in range(i + 1, n):
                if rebuilt[j] > rebuilt[i]:
                    tot += 1
            if tot != ri[i]:
                notp = True
                break

    if notp:
        print("NO")
    else:
        print("YES")
        print(*rebuilt)


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)