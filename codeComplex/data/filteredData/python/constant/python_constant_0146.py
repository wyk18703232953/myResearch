import random

def primecheck(x):
    cnt = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            cnt += 1
            break
    if cnt:
        return 1
    else:
        return 0


def main(n):
    # 若 n 过小或者为奇数，无法找到两个合数之和，直接返回
    if n < 8 or n % 2 == 1:
        print("No valid composite pair for n =", n)
        return

    for i in range(4, n):
        if primecheck(i) == 1 and primecheck(n - i) == 1:
            print(str(i) + " " + str(n - i))
            break


# 示例：自动生成测试数据并调用 main
if __name__ == "__main__":
    # 生成一个大于等于 8 的偶数，作为测试规模 n
    n = random.randint(8, 100)
    if n % 2 == 1:
        n += 1
    main(n)