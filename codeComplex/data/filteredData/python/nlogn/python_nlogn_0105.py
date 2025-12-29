import random

def main(n):
    # 根据 n 生成测试数据：长度为 n 的随机整数数组
    # 你可以根据需要调整数据范围
    arr = [random.randint(0, 100) for _ in range(n)]

    new = sorted(arr)
    count = 0

    for i in range(n):
        if arr[i] != new[i]:
            count += 1

    if count <= 2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)