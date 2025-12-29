import random

def main(n):
    # 生成 n 个随机整数作为测试数据
    # 数值范围可根据需要调整
    data = [random.randint(1, 100) for _ in range(n)]
    
    # 原始逻辑开始
    list_ = sorted(set(data))
    if len(list_) == 1:
        print("NO")
    else:
        print(list_[1])

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)