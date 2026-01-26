def main(n):
    # 确定性构造 s，保证与 n 有关联且规模合理
    s = n * (n + 1) // 2

    count = 0
    for i in range(n):
        count += s // (n - i)
        s -= (s // (n - i)) * (n - i)
    return count

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行实验
    result = main(10)
    # print(result)
    pass