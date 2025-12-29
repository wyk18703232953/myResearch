import random

def main(n):
    # 生成测试数据：长度为 n 的随机数组，元素范围可根据需要调整
    a = [random.randint(0, 100) for _ in range(n)]

    fl = False
    ans = True
    for i in range(n - 1):
        if a[i + 1] > a[i]:
            if fl:
                ans = False
        else:
            fl = True

    if ans:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)