import random

def main(n):
    # 根据规模 n 生成测试数据，这里生成两个不超过 n 的随机非负整数 l, r
    l = random.randint(0, n)
    r = random.randint(0, n)
    
    x = l ^ r
    pow_val = 1
    while pow_val <= x:
        pow_val *= 2
    return pow_val - 1

# 示例：直接运行文件时做一次示例调用
if __name__ == "__main__":
    n = 10**6  # 可根据需要修改规模
    ans = main(n)
    print(ans)