import random

def main(n):
    # 生成测试数据：sequence 长度为 n，fingerprint 长度为 m（这里取 m = n // 2）
    m = max(1, n // 2)

    # 为避免过大整数，限制取值范围
    max_value = max(10, n * 2)

    # 随机生成由数字字符串组成的 sequence 和 fingerprint
    sequence = [str(random.randint(0, max_value)) for _ in range(n)]
    fingerprint = [str(random.randint(0, max_value)) for _ in range(m)]

    # 保持与原逻辑一致：输出 sequence 中出现在 fingerprint 中的元素（按 sequence 顺序）
    result = " ".join(i for i in sequence if i in fingerprint)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    main(10)