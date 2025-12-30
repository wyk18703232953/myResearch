import random

def main(n: int):
    # 生成测试数据：长度为 n 的非负整数列表
    # 这里生成 0 到 n 之间的随机数，可根据需要调整
    lst = [random.randint(0, n) for _ in range(n)]

    st = set()
    flag = False
    count = 0
    lol = None

    for i in lst:
        if i not in st:
            st.add(i)
        else:
            flag = True
            count += 1
            lol = i

    sum1 = n * (n - 1) // 2

    if count > 1:
        print('cslnb')
        return

    if not flag:
        if (sum(lst) - sum1) % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')
    else:
        if (lol - 1) in lst or lol == 0:
            print('cslnb')
        else:
            if (sum(lst) - sum1) % 2 == 0:
                print('cslnb')
            else:
                print('sjfnb')


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)