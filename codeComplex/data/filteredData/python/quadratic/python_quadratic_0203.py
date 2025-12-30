import random

def main(n):
    # 随机生成一个 n x m 的 0/1 字符矩阵，m 可按需要定义，这里令 m = n
    m = n

    # 生成测试数据 X（列表的列表，元素为'0'或'1'的字符）
    X = []
    for _ in range(n):
        row = [str(random.randint(0, 1)) for _ in range(m)]
        X.append(row)

    # 统计每一列中 '1' 的数量
    nums = []
    for col in range(m):
        t = 0
        for row in range(n):
            t += int(X[row][col])
        nums.append(t)

    # 按原逻辑判断是否存在某一行满足条件
    for i in range(n):
        ok = True
        for j in range(m):
            if X[i][j] == '1':
                if nums[j] > 1:
                    continue
                else:
                    ok = False
                    break
        if ok:
            print("YES")
            return
    print("NO")