import random

def main(n):
    # 根据规模 n 生成测试数据（此处仅作为示例：生成 n 个随机整数）
    data = [random.randint(1, 100) for _ in range(n)]
    # 原始逻辑：固定输出 25
    print(25)

if __name__ == "__main__":
    # 示例：调用 main，规模可按需调整
    main(10)