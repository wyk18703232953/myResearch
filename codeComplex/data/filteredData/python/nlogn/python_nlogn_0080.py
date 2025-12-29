import random

def main(n):
    # 生成测试数据
    # x 在 [1, n] 范围内
    x = random.randint(1, n)

    a = []
    k = {}
    for _ in range(n):
        # 生成 p, q，范围可根据需要调整
        p = random.randint(1, n // 2 + 1)
        q = random.randint(1, 100)
        if p not in k:
            k[p] = 1
        a.append([p, q])

    # 以下为原逻辑的无 input() 版本
    a.sort()
    k_sorted_keys = sorted(k.keys())[::-1]

    p_list = []
    for key in k_sorted_keys:
        for item in a:
            if item[0] == key:
                p_list.append(item)

    if 1 <= x <= len(p_list):
        result = p_list.count(p_list[x - 1])
    else:
        result = 0

    # 按原程序行为，只打印结果
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)