import random

def main(n):
    # 1. 根据 n 生成测试数据
    # 这里生成一个长度为 n 的随机数组，元素值在 1 到 n 之间
    arr = [random.randint(1, n) for _ in range(n)]

    # 2. 原逻辑开始
    arr2 = sorted(arr)
    count = 0
    a = 0

    # 拷贝一份数组，用于模拟原始逻辑中的原地修改
    work_arr = arr[:]

    for i in range(n):
        if work_arr[i] != arr2[i]:
            count += 1
            k = work_arr[i]
            work_arr[i] = arr2[i]
            z = work_arr.index(arr2[i])
            work_arr[z] = k

        if count > 2:
            a = 1
            break

    if a == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)