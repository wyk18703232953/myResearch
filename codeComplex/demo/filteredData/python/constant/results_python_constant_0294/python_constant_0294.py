import math

def main(n):
    # n 作为规模参数，这里构造确定性的 k, planes_n, s, p
    # 保证 s、p 不为 0 且有一定变化
    k = n + 1               # number of persons
    planes_n = n + 2        # planes each will make
    s = (n % 5) + 1         # planes per sheet, in [1,5]
    p = (n % 7) + 1         # sheets per pack, in [1,7]

    sheet_for_each_person = math.ceil(planes_n / s)
    total_sheets_required = k * sheet_for_each_person
    no_of_packs = math.ceil(total_sheets_required / p)
    # print(no_of_packs)
    pass
if __name__ == "__main__":
    main(10)