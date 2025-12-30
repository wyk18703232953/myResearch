import random

def main(n: int) -> int:
    # 根据 n 生成测试数据，这里直接使用传入的 n
    # 若需要更复杂的测试数据生成逻辑，可在此扩展
    rang = list(range(2, n // 2 + 1))
    a = [i * (n // i - 1) for i in rang]
    result = sum(a) * 4
    print(result)
    return result

if __name__ == "__main__":
    # 示例：自动生成一个规模 n（可根据需要修改范围）
    test_n = random.randint(2, 10**6)
    main(test_n)