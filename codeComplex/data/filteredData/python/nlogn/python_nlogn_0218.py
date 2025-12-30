import random

def main(n):
    # 生成测试数据
    # 这里假设原始数据为非负整数，范围可自行调整
    u = random.randint(1, 1000)
    # 保证 n >= 2 才有意义
    if n < 2:
        print("-1")
        return

    # 生成随机数组，元素范围 [0, 10000]
    arr = sorted(random.randint(0, 10000) for _ in range(n))

    # 以下为原逻辑（去掉 input() 部分）
    j, i = 1, 0
    maxi = -1
    flag = 0

    for i in range(n - 1):
        if arr[i + 1] - arr[i] <= u:
            flag = 1
    if flag == 0:
        print("-1")
        return

    i = 0
    while i < n - 2:
        while True:
            if j >= n:
                j = n - 1
                break
            if arr[j] - arr[i] > u:
                j -= 1
                break
            j += 1
        if i == j:
            j += 1
        elif arr[j] == arr[i]:
            pass
        elif arr[j] - arr[i] <= u:
            maxi = max(maxi, (arr[j] - arr[i + 1]) / (arr[j] - arr[i]))
        i += 1

    if maxi == 0:
        print("-1")
    else:
        print(maxi)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)