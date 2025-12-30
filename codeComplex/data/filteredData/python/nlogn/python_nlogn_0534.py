import random

def main(n):
    # 生成测试数据：k 和数组 arr
    # 这里示例选择：
    #   1 <= k <= 10^9，避免为 0
    #   数组元素在 [1, 10^9] 范围内
    random.seed(0)  # 固定随机种子便于复现
    k = random.randint(1, 10**9)
    arr = [random.randint(1, 10**9) for _ in range(n)]

    # 以下为原逻辑的封装
    d = [{} for _ in range(11)]
    for i in range(n):
        st = arr[i]
        for j in range(11):
            r = st % k
            try:
                d[j][r] += 1
            except KeyError:
                d[j][r] = 1
            st *= 10

    count_pair = 0
    for i in arr:
        st = str(i)
        l = len(st)
        mod_st = (k - (i % k)) % k
        if mod_st in d[l]:
            count_pair += d[l][mod_st]
            if int(st + st) % k == 0:
                count_pair -= 1

    print(count_pair)


# 示例：执行 main，n 为规模
if __name__ == "__main__":
    main(10)