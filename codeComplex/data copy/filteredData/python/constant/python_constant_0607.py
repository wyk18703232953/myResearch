def main(n):
    # 这里根据 n 生成一个与规模相关的 k
    # 可按需要调整生成规则
    k = max(1, n // 3)

    result = ((n * 2) // k + bool((n * 2) % k) +
              (n * 5) // k + bool((n * 5) % k) +
              (n * 8) // k + bool((n * 8) % k))

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：可在此处指定 n 的测试规模
    main(10)