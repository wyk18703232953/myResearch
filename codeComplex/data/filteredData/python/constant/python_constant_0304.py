import math
import random

def main(n):
    # 生成测试数据：
    # people: 1 ~ n
    # planes_each: 1 ~ n
    # per: 1 ~ n
    # sheets: 1 ~ n
    people = random.randint(1, n)
    planes_each = random.randint(1, n)
    per = random.randint(1, n)
    sheets = random.randint(1, n)

    sheets_per_person = math.ceil(planes_each / per)
    needed = sheets_per_person * people
    packs = math.ceil(needed / sheets)
    print(packs)


if __name__ == "__main__":
    # 示例调用，规模可调
    main(100)