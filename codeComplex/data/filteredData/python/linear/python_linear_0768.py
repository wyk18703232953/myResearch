import random

def main(n):
    # 1. 生成测试数据
    #   - n: 数组大小
    #   - q: 询问次数，这里设为 n，若需可自行调整为其它函数关系
    q = n
    # 生成一个随机数组，元素范围可根据需求调整
    arr = [random.randint(1, 10**6) for _ in range(n)]

    # 2. 原始逻辑开始（移除了 input()，使用上述生成的数据）
    arr = arr[:]  # 确保是可修改的列表
    for _ in range(n):
        arr.append(0)

    ind = arr.index(max(arr))
    ans = []
    ptr1 = 0
    ptr2 = n

    # 预处理阶段：构造前 ind 次比较的答案
    for _ in range(ind):
        ans.append([arr[ptr1], arr[ptr1 + 1]])
        if arr[ptr1] > arr[ptr1 + 1]:
            arr[ptr2] = arr[ptr1 + 1]
            arr[ptr1 + 1] = arr[ptr1]
        else:
            arr[ptr2] = arr[ptr1]
        ptr1 += 1
        ptr2 += 1

    # 3. 构造 q 个查询，并输出结果
    #   - 这里将查询 m 也随机生成在 [1, 2*n] 范围内
    queries = [random.randint(1, 2 * n) for _ in range(q)]

    for m in queries:
        if m <= ind:
            print(*ans[m - 1])
        else:
            mm = m - ind
            mm = mm % (n - 1)
            if mm == 0:
                mm += n - 1
            print(arr[ind], arr[ind + mm])


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要修改 n
    main(5)