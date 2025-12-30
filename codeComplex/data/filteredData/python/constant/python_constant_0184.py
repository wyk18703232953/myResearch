import random

def main(n: int):
    # 根据 n 生成测试数据（此处示例：生成 n 个 1~100 的随机整数）
    test_data = [random.randint(1, 100) for _ in range(n)]
    
    # 原程序逻辑：固定输出 25
    # 为了保持语义一致，这里仍然只输出 25
    print(25)

if __name__ == "__main__":
    # 示例：可手动修改 n 测试
    main(10)