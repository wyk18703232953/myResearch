import random

def main(n):
    # 生成 1..n 的随机排列作为测试数据
    w = list(range(1, n + 1))
    random.shuffle(w)

    # 原逻辑开始
    c = {w[j]: j + 1 for j in range(n)}
    res = 0
    for j in range(1, n + 1):
        if w[j - 1] == j:
            continue
        else:
            res += 1
            y = w[j - 1]
            w[j - 1] = j
            w[c[j] - 1] = y
            r = c[j]
            c[j] = j
            c[y] = r

    if n % 2 == 0:
        if res % 2 == 0:
            print("Petr")
        else:
            print("Um_nik")
    else:
        if res % 2:
            print("Petr")
        else:
            print("Um_nik")

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)