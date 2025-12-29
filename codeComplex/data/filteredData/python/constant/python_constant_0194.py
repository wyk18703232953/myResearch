import random

def main(n):
    # 这里根据 n 生成测试数据（示例：生成 n 个 1~100 的随机整数）
    data = [random.randint(1, 100) for _ in range(n)]
    
    # 原始程序逻辑：固定输出 25
    print(25)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可以根据需要修改
    main(10)