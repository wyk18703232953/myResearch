import random

def main(n):
    # 生成测试数据：长度为 n 的数组，元素为随机整数
    # 范围可根据需要调整，这里设为 [-10**6, 10**6]
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    # 预计算所有不超过 10**18 的 2 的幂
    k = []
    i = 0
    while 2 ** i <= 10**18:
        k.append(2 ** i)
        i += 1

    # 统计各元素频次
    d = {}
    s1 = set()
    for v in arr:
        s1.add(v)
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1

    # 找出不能与任何另一个数配对成 2 的幂的元素
    s2 = set()
    for val in s1:
        flag = False
        for p in k:
            x = p - val
            y = d.get(x, -1)
            if y != -1:
                # 若需要配对的是自身且只有一个，不能算
                if x == val and d[val] == 1:
                    continue
                flag = True
                break
        if not flag:
            s2.add(val)

    res = 0
    for v in s2:
        res += d[v]

    print(res)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)