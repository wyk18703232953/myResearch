import random

def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的整数列表
    # 这里示例生成 -n 到 n 之间的随机整数
    l = [random.randint(-n, n) for _ in range(n)]
    
    s = set(l)
    if 0 in s:
        print(len(s) - 1)
    else:
        print(len(s))

if __name__ == "__main__":
    # 示例：使用 n = 10 调用主函数
    main(10)