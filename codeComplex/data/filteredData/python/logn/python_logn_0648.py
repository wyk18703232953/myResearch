import random

def wzor(n):
    return (n * (n + 1)) / 2

def mafia(n, c):
    po = 1
    ko = n
    sr = (po + ko) // 2
    while po != ko:
        if wzor(sr) - (n - sr) >= c:
            ko = sr
        else:
            po = sr + 1
        sr = (po + ko) // 2

    return int(wzor(po) - c)

def main(n):
    # 根据规模 n 生成测试数据
    # 保证 c 合理：0 <= c <= wzor(n)
    max_c = int(wzor(n))
    c = random.randint(0, max_c)
    
    result = mafia(n, c)
    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)