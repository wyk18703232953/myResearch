import random

def main(n: int):
    # 根据规模 n 生成一个随机整数作为测试数据
    # 这里假设输入规模就是整数的最大值上界
    if n <= 0:
        return 0

    i = random.randint(0, n)
    result = (i // 2) * 3
    print(result)
    return result

if __name__ == "__main__":
    # 示例：使用 n=100 作为规模运行
    main(100)