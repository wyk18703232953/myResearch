from math import ceil

def main(n):
    # 将 n 映射为原程序的四个参数 k, n_people, s, p
    # 保证均为正整数且随 n 有规律变化
    k = n % 10 + 1          # 1 ~ 10
    n_people = n * 10 + 1   # 随 n 增长的需要抄写的人数
    s = n % 7 + 1           # 每人一张纸可写的页数，1 ~ 8
    p = (n % 5) + 1         # 每包纸张数，1 ~ 5

    n_sheets = ceil(n_people / s) * k
    n_p = ceil(n_sheets / p)
    # print(n_p)
    pass
if __name__ == "__main__":
    main(100)