import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 原逻辑中只用到了 n 和 k，这里我们让 k 在一个相对于 n 较大的范围内随机生成
    # 例如：k 在 [0, n * 10^12] 范围内取一个整数
    max_height = 10**12
    k = random.randint(0, n * max_height)

    def area(height):
        return n * height

    def bin_search(low, high):
        if high == low:
            return high
        if high - low == 1:
            if area(low) >= k:
                return low
            return high
        midd = (high + low) // 2
        if area(midd) > k:
            return bin_search(low, midd)
        return bin_search(midd, high)

    # 二分搜索上界可以按原代码给的一个足够大的值
    result = bin_search(0, 10**18)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(10)