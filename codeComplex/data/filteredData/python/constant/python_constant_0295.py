from math import ceil

def main(n):
    # 将 n 映射为原程序的四个参数 k, n_people, s, p
    # 保证参数均为正整数且随 n 规模化
    k = max(1, n // 3)
    n_people = max(1, n)
    s = max(1, n // 2)
    p = max(1, n // 4)

    sheetsforone = ceil(n_people / s)
    sheetsfork = sheetsforone * k
    packs = ceil(sheetsfork / p)
    # print(int(packs))
    pass
if __name__ == "__main__":
    main(1000)