import random

def main(n):
    # 1. 生成测试数据
    #    原程序读取：n, k 和一个长度为 n 的数组 arr
    #    这里生成：
    #       k: 随机取 [1, n]（原代码中实际上未使用 k，只保持接口一致）
    #       arr: 长度为 n，元素取值范围 [1, 100]
    k = random.randint(1, max(1, n))
    arr = [random.randint(1, 100) for _ in range(n)]

    # 2. 统计每个数字出现次数
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # 3. 按原逻辑从 100 到 1 枚举 i，计算可以分成多少组大小为 i
    flag = True
    for i in range(100, 0, -1):
        t2 = 0
        for j in d.values():
            t2 += j // i
        if t2 >= n:
            print(i)
            flag = False
            break

    if flag:
        print(0)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小
    main(10)