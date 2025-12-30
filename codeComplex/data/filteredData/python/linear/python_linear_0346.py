import random

def main(n: int):
    # 生成测试数据：a 在 [0, n] 范围内，b 在 [1, n] 范围内（虽然原逻辑未使用 b，但保留生成）
    a = random.randint(0, n)
    b = random.randint(1, n)

    q, r = divmod(a, 2)
    result = '01' * q + '0' * r
    print(result)

if __name__ == "__main__":
    # 示例：可自行修改规模 n
    main(10)