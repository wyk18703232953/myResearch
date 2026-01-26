def main(n):
    # 核心逻辑保持不变：原本从 input() 读取的 n 现在直接由参数 n 提供
    result = (n + n % 2) * ((n + 2) // 2) // 2
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)