import random

def main(n):
    # 生成测试数据：n 个非负整数
    # 这里生成范围 [0, 2*n] 的随机数字，你可以按需调整
    a = [random.randint(0, 2 * n) for _ in range(n)]

    summ = 0
    a.sort()
    if len(a) == 1:
        if a[0] % 2 == 1:
            print('sjfnb')
        else:
            print('cslnb')
    elif a[0] == a[1] == 0:
        print('cslnb')
    else:
        x = False
        for i in range(2, n):
            if a[i] == a[i - 1] and a[i - 1] == a[i - 2]:
                x = True
        if x:
            print('cslnb')
        else:
            x = False
            for i in range(2, n):
                if a[i] == a[i - 1] and a[i] - 1 == a[i - 2]:
                    x = True
            if x:
                print('cslnb')
            else:
                summ = 0
                for i in range(1, n):
                    if a[i] == a[i - 1]:
                        summ += 1
                if summ > 1:
                    print('cslnb')
                else:
                    summ = 0
                    for i in range(n):
                        summ += a[i] - i
                    if summ % 2 == 0:
                        print('cslnb')
                    else:
                        print('sjfnb')


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)