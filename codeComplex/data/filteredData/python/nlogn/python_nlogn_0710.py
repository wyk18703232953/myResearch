import random

def main(n: int):
    # 生成测试数据：n个非负整数，这里生成在[0, 2n]区间内
    u = [random.randint(0, 2 * n) for _ in range(n)]

    u.sort()
    ans = 0
    k = 1
    ok = False

    for i in range(1, n):
        if u[i] == u[i - 1]:
            k += 1
            if k == 3:
                print('cslnb')
                return
            if k == 2:
                if ok or u[i] == 0 or u[i] - u[i - 2] == 1:
                    print('cslnb')
                    return
                ok = True
        else:
            k = 1

    for i in range(n):
        ans += u[i] - i

    if ans % 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)