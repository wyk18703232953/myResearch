def num_ops(low, high):
    if high % low == 0:
        return high // low

    else:
        return (high // low) + num_ops(high % low, low)

def main(n):
    # 生成 n 组 (low, high) 数据
    # 确保 low <= high 且 low > 0
    results = []
    for i in range(1, n + 1):
        low = i
        high = 2 * i + (i % 3)  # 可扩展的确定性构造
        if low == 0:
            low = 1
        if high < low:
            high = low
        results.append(num_ops(low, high))
    # 保持与原程序类似的输出行为
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)