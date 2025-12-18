# -*-coding:utf-8-*-
def solution():
    k = int(input())
    k -= 1 # 字符串起始从0
    n, m = 1, 9
    while k > n*m:
        k, n, m = k - n*m, n+1, m*10
        # n记录属于哪一个区段，m记录这个区段内小段数
        # 1位 1x1x9  2位  2x10x9  3位  3x100x9
    x = str(10**(n-1) + k//n)[k % n]
    # 10**(n-1) + k//n计算是哪一个整数
    print(x)


if __name__ == "__main__":
    solution()

