import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 a
    # 这里生成 0 到 n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    pro = n * (n - 1) // 2
    dic = {}
    for item in a:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1

    counter = 0
    for item in dic:
        if 0 in dic and dic[0] >= 2:
            print('cslnb')
            break
        if dic[item] > 2:
            print('cslnb')
            break
        elif dic[item] == 2:
            if counter == 1 or item - 1 in dic:
                print('cslnb')
                break
            else:
                counter = 1
    else:
        if (sum(a) - pro) % 2 == 1:
            print('sjfnb')
        else:
            print('cslnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)