import random

def main(n):
    # 生成测试数据：长度为 n 的整数数组 a
    # 这里生成 0 到 2n 之间的随机整数，可根据需要修改
    a = [random.randint(0, 2 * n) for _ in range(n)]

    dupes = 0
    dupeVal = -1
    d = set()
    for el in a:
        if el in d:
            dupes += 1
            dupeVal = el
        else:
            d.add(el)

    inPlay = True
    if dupes > 1:
        print('cslnb')
        inPlay = False
    elif dupes == 1:
        if dupeVal == 0 or (dupeVal - 1) in d:
            print('cslnb')
            inPlay = False

    if inPlay:
        finalSum = (n * (n - 1)) // 2
        Sum = sum(a)
        if (Sum - finalSum) % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)