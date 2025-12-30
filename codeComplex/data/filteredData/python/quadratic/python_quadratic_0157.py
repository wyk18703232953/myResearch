import random

def main(n):
    # 生成测试数据：n 和 k，以及长度为 n 的数组 arr
    # 这里设定元素范围在 [0, 255] 以内，k 在 [1, 260] 以内，以符合原程序中 260 的大小限制
    k = random.randint(1, 260)
    arr = [random.randint(0, 255) for _ in range(n)]

    par = [i for i in range(260)]
    path = [-1 for _ in range(260)]

    for i in range(n):
        j = arr[i]
        if path[j] >= 0:
            par[j] = par[path[j]]
            continue
        jump = 1
        while j > 0 and path[j] == -1 and jump < k:
            path[j] = arr[i]
            j -= 1
            jump += 1
        if arr[i] - par[j] + 1 <= k:
            par[arr[i]] = par[j]
            path[j] = arr[i]
        else:
            par[arr[i]] = par[j + 1]

    for i in range(n):
        print(par[arr[i]], end=' ')
    print()


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)