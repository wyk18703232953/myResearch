import random

def ballbuster5000(arr, rj):
    for i in arr:
        rj += i
    gg = 0
    i = 0
    while gg <= rj and i < len(arr):
        gg += arr[i]
        rj -= arr[i]
        i += 1
    return i

def main(n):
    # 根据规模 n 生成测试数据：n 个随机正整数
    # 可以根据需要调整数据范围
    x = [random.randint(1, 1000) for _ in range(n)]
    x.sort(reverse=True)
    result = ballbuster5000(x, 0)
    print(result)

if __name__ == "__main__":
    # 示例：手动指定 n 的值进行运行
    main(10)