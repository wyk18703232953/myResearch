import random

def main(n):
    # n 为规模，这里将其作为 m（向量个数）
    m = n

    # 生成测试数据：随机生成 m 个整数
    # 为了与原代码位宽匹配，使用 0 ~ (1 << 20) - 1 范围内的整数
    # 可根据需要调整位宽
    arr = [random.randint(0, (1 << 20) - 1) for _ in range(m)]

    buck = [[0, 0] for _ in range(2201)]

    for i in range(m):
        a = arr[i]
        ok = True
        br = 0
        for j in range(2200, -1, -1):
            if a & (1 << j):
                if buck[j][0]:
                    a ^= buck[j][0]
                    br ^= buck[j][1]
                else:
                    ok = False
                    buck[j][0] = a
                    buck[j][1] = br | (1 << i)
                    break
        if not ok:
            print("0")
        else:
            lst = []
            for j in range(2201):
                if br & (1 << j):
                    lst.append(j)
            print(len(lst), end=' ')
            for j in lst:
                print(j, end=' ')
            print()

if __name__ == "__main__":
    # 示例：运行 main，规模 n 可按需调整
    main(5)