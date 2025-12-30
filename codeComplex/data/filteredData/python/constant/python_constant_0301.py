import random
import math

def main(n):
    # 生成测试数据：
    # k: 参加的人数 (1 ~ n)
    # n: 每人需要的页数 (1 ~ n)
    # s: 每包纸张中的页数 (1 ~ n)
    # p: 每包纸张的本数 (1 ~ n)
    k = random.randint(1, n)
    need_pages = random.randint(1, n)
    s = random.randint(1, n)
    p = random.randint(1, n)

    # 计算总共需要的本数
    total_sheets_per_person = (need_pages + s - 1) // s  # 每人需要的包数（向上取整）
    total_sheets = total_sheets_per_person * k          # 总包数
    result = (total_sheets + p - 1) // p                # 需要的本数（向上取整）

    print(result)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的规模
    main(100)