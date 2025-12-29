import random

def main(n):
    # 生成测试数据：n 个非负整数
    # 可以根据需要调整数据范围，这里设为 [0, 2n]
    arr = [random.randint(0, 2 * n) for _ in range(n)]

    dic = {}
    for val in arr:
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] += 1

    flag1 = True
    if 0 in dic:
        if dic[0] >= 2:
            flag1 = False

    cnt = 0
    for val in dic.keys():
        if dic[val] >= 3:
            flag1 = False
            break
        if dic[val] == 2:
            cnt += 1
            if val - 1 in dic:
                flag1 = False
                break

    if cnt >= 2:
        flag1 = False

    if flag1 is False:
        print('cslnb')
    else:
        flag2 = (n * (n - 1) // 2 + sum(arr)) % 2
        if flag2 == 1:
            print('sjfnb')
        else:
            print('cslnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)