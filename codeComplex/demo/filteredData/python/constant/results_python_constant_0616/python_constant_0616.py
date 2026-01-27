import math

def main(n):
    # n 表示测试用例数量
    results = []
    for i in range(n):
        # 确定性生成 l, r
        # 让区间规模随 n 和 i 线性增长，便于规模化实验
        l = i + 1
        r = (i + 1) * 3

        l -= 1
        war1 = math.ceil(l / 2)
        if l % 2 == 1:
            war1 = -1 * war1

        war2 = math.ceil(r / 2)
        if r % 2 == 1:
            war2 = -1 * war2

        results.append(war2 - war1)
    return results

if __name__ == "__main__":
    # 示例调用：规模 n = 10
    ans = main(10)
    for v in ans:
        # print(v)
        pass