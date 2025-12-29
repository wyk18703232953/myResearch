import random

def main(n: int):
    # 根据 n 生成测试数据，这里示例为生成一个长度为 n 的随机整数数组
    # 实际生成逻辑可按需要修改，这里只是占位示例
    test_data = [random.randint(0, 100) for _ in range(n)]
    
    # 保留原有输出逻辑，这里按照原逻辑只用到 n
    print(f"0 0 {n}")
    
    # 如需使用 test_data，可在此处添加相应处理逻辑
    return test_data

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)