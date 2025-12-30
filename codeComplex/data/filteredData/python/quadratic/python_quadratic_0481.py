import random

def main(n: int):
    # 生成一个满足条件的随机数组 arr（1..n 的一个排列）
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    # 根据 arr 计算 left 和 right
    left = [0] * n
    right = [0] * n
    for i in range(n):
        more_left = 0
        for j in range(i):
            if arr[j] > arr[i]:
                more_left += 1
        left[i] = more_left

        more_right = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                more_right += 1
        right[i] = more_right

    # 还原 rank、再计算 arr2，并用原逻辑校验
    rank = [x + y for (x, y) in zip(left, right)]
    arr2 = [(n - r) for r in rank]

    # check left
    for i in range(n):
        more = 0
        for j in range(i):
            if arr2[j] > arr2[i]:
                more += 1
        if more != left[i]:
            print('NO')
            return

    # check right
    for i in range(n):
        more = 0
        for j in range(i + 1, n):
            if arr2[j] > arr2[i]:
                more += 1
        if more != right[i]:
            print('NO')
            return

    print('YES')
    for x in arr2:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    # 示例：规模为 5
    main(5)