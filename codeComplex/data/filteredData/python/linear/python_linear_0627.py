import random

def main(n):
    # 生成测试数据
    # 让 m 与 n 同规模
    m = max(1, n)

    # 生成严格递增的数组 arr，长度为 n
    # arr[i] 范围 [1, 10*n]，保证递增
    arr = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)
        arr.append(cur)

    # 生成 t 数组，长度为 n，值为 0 或 1，确保至少有一个 1
    t = [random.randint(0, 1) for _ in range(n)]
    if 1 not in t:
        t[random.randrange(n)] = 1

    # 原逻辑开始
    taxi = []
    for i in range(len(arr)):
        if t[i] == 1:
            taxi.append(arr[i])

    taxi2 = []
    kek = 1
    for i in range(len(taxi) - 1):
        mid = taxi[i] + (taxi[i + 1] - taxi[i]) // 2
        taxi2.append([kek, mid])
        kek = mid + 1
    taxi2.append([kek, arr[-1]])

    taxi3 = [0] * m
    j = 0
    for i in range(len(arr)):
        if j + 1 < len(taxi2) and arr[i] > taxi2[j][1]:
            j += 1
        if t[i] != 1 and j < m:
            taxi3[j] += 1

    print(" ".join(map(str, taxi3)))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)