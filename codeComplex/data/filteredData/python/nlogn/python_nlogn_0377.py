import random

def main(n):
    # 生成测试数据
    # 随机生成 k，范围可根据需要调整
    k = random.randint(0, 10)
    # 生成 n 个随机整数，范围可根据需要调整
    arr = [random.randint(0, 100) for _ in range(n)]

    # 原始逻辑
    arr.sort()
    c = n
    j = 0
    for x in arr:
        while j < n and x > arr[j]:
            if x - arr[j] <= k:
                c -= 1
            j += 1

    print(c)

if __name__ == "__main__":
    # 示例调用，n 可按需修改
    main(10)