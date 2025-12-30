import random

def solve(n, v):
    fuel = min(n - 1, v)
    cost = fuel
    for i in range(2, n):
        if fuel >= n - 1:
            break
        fuel += 1
        cost += i
    return cost

def main(n):
    # 根据规模 n 生成测试数据
    # 约束：1 <= v <= n（与原题直观相符）
    if n <= 1:
        n = 2  # 保证有意义的规模
    v = random.randint(1, n)
    
    result = solve(n, v)
    print(result)

# 示例调用
if __name__ == "__main__":
    main(10)