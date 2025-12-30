def fn(n):
    return (n * (n + 1)) // 2

def search(x, n):
    left, right = 0, n
    while left <= right:
        middle = left + (right - left) // 2
        value = fn(middle) - (n - middle)
        if value == x:
            return n - middle
        elif value > x:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def main(n):
    # 生成测试数据：
    # 这里构造一个 x，使得一定有解：
    # 取某个 middle0，在 [0, n] 范围内
    middle0 = n // 2
    x = fn(middle0) - (n - middle0)  # 根据原公式反推得到对应的 x

    result = search(x, n)
    print(result)

if __name__ == "__main__":
    # 示例：可以根据需要调整 n 的规模
    main(10)