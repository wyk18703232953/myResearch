import random

def main(n: int):
    # 1. 随机生成 s
    # 让 s 在 [0, 10^6] 范围内
    s = random.randint(0, 10**6)

    # 2. 随机生成 n 行 [a_i, b_i]
    # 假设 a_i 在 [0, s]，b_i 在 [0, 10^6]
    lst = []
    for _ in range(n):
        a = random.randint(0, s)
        b = random.randint(0, 10**6)
        lst.append([a, b])

    # 3. 原始逻辑
    lst = sorted(lst, key=lambda x: x[0], reverse=True)
    prev, ans = s, 0
    for i in range(n):
        ans += prev - lst[i][0]
        if ans < lst[i][1]:
            ans += (lst[i][1] - ans)
        prev = lst[i][0]
    print(ans + prev)


if __name__ == "__main__":
    # 示例：用 n = 10 运行
    main(10)