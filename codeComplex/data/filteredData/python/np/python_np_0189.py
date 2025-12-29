import random

def isValid(arr, l, r, x):
    return l <= sum(arr) <= r and max(arr) - min(arr) >= x

def main(n):
    # 生成测试数据
    random.seed(0)
    # 确保有意义的范围与差值
    l = random.randint(1, 10 * n)
    r = l + random.randint(0, 10 * n)
    x = random.randint(0, 10)
    arr = [random.randint(1, 50) for _ in range(n)]

    valid = 0
    for i in range(1, 1 << n):
        temp = []
        for j in range(n):
            if (i >> j) & 1:
                temp.append(arr[j])
        if isValid(temp, l, r, x):
            valid += 1
    print(valid)

if __name__ == "__main__":
    main(5)