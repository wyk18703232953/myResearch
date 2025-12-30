import random

def main(n: int):
    # 1. 根据 n 生成测试数据
    # 这里生成 n 个范围在 [-10^9, 10^9] 的随机整数
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 2. 原始逻辑开始
    maxval = max(arr)
    maxindex = -1
    for i in range(n):
        if arr[i] == maxval:
            maxindex = i
            break

    flag = 0
    temp = maxval
    for i in range(maxindex - 1, -1, -1):
        if temp <= arr[i]:
            flag = 1
            break
        else:
            temp = arr[i]

    temp = maxval
    for i in range(maxindex + 1, n):
        if arr[i] >= temp:
            flag = 1
            break
        else:
            temp = arr[i]

    if flag == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)