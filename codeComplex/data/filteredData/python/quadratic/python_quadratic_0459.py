import random

def main(n):
    # 生成测试数据：长度为 n 的正整数数组 a
    # 这里生成 1~n 范围内的随机整数，确保每个元素 >= 1
    random.seed(0)
    a = [random.randint(1, n) for _ in range(n)]

    h = [-1] * n
    b = [(a[i], i) for i in range(n)]
    b.sort(reverse=True)

    for e in b:
        num, idx = e
        flag = True  # 原代码中未使用，保留不影响逻辑
        allNeg = True
        foundLosing = False
        foundWin = False
        for i in range(idx % num, n, num):
            if i == idx:
                continue
            if h[i] != -1:
                allNeg = False
            if h[i] == 0:
                foundLosing = True
                break
            if h[i] == 1:
                foundWin = False
        if allNeg:
            h[idx] = 0
        elif foundLosing:
            h[idx] = 1
        else:
            h[idx] = 0

    # 输出结果
    for i in range(n):
        if h[i] == 0:
            print('B', end='')
        else:
            print('A', end='')

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)