import random

def main(n):
    # 生成测试数据
    # a,b 在 [0, n]
    a = random.randint(0, n)
    b = random.randint(0, n)
    # x,y,z 在 [0, n]
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    # 原逻辑
    ans = max(0, 2 * x + y - a) + max(0, 3 * z + y - b)
    print(ans)

if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)