import math
import random

def main(n):
    """
    n: 规模参数，用于生成测试数据。此处我们用 n 控制人数 k 的大小。
    其他参数按合理范围随机生成：
      - k: 1 ~ n
      - 每人需要制作的纸飞机数量 n_planes: 1 ~ max(1, n)
      - 每张纸能折的飞机数 s: 1 ~ 10
      - 每包纸张数 p: 1 ~ 50
    """
    # 生成测试数据
    k = random.randint(1, max(1, n))          # no of person
    n_planes = random.randint(1, max(1, n))   # no of planes each will make
    s = random.randint(1, 10)                 # no of planes that can be made in one sheet
    p = random.randint(1, 50)                 # no of sheet in one pack

    sheet_for_each_person = math.ceil(n_planes / s)
    total_sheets_required = k * sheet_for_each_person
    no_of_packs = math.ceil(total_sheets_required / p)

    print(no_of_packs)

if __name__ == "__main__":
    # 示例调用：可以根据需要修改规模参数
    main(10)