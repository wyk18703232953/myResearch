import random

def main(n):
    # 生成测试数据：n 个随机整数
    values = [random.randint(0, 100) for _ in range(n)]
    
    wrong = 0
    sorted_values = sorted(values)
    for i in range(n):
        if values[i] != sorted_values[i]:
            wrong += 1
    if wrong > 2:
        print("NO")
    else:
        print("YES")

# 示例调用
if __name__ == "__main__":
    main(10)