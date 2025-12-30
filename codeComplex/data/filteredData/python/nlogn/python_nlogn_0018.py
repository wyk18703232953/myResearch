import random

def main(n):
    # 生成测试数据：n个随机整数，范围可根据需要调整
    # 这里设置为 1 到 100 之间
    x = [random.randint(1, 100) for _ in range(n)]
    
    # 原始逻辑开始
    x = list(set(x))
    x.sort()
    if len(x) != 1:
        print(x[1])
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)