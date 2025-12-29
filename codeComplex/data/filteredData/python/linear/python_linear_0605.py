import random

def main(n):
    # 根据 n 生成测试数据：这里直接使用参数 n 作为规模
    # 若需要随机或其他方式生成，可在此处修改生成逻辑
    print('0 0')
    n -= 1
    k = n // 2
    p = n - k
    x = -k // 2
    while k > 0:
        if x != 0:
            print(x, 0)
            k -= 1
        x += 1
    y = -p // 2
    while p > 0:
        if y != 0:
            print(0, y)
            p -= 1
        y += 1

if __name__ == "__main__":
    # 示例：自动选择一个规模 n 进行测试
    # 可根据需要修改，这里给一个固定或随机的 n
    test_n = 10  # 例如固定为 10
    # test_n = random.randint(1, 20)  # 或者使用随机规模
    main(test_n)