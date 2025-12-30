import random

def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的正整数列表
    # 这里假设原题中 k 是一个长度不定的正整数数组
    # 随机生成范围可按需要调整
    k = [random.randint(1, 10) for _ in range(n)]
    
    # 逻辑与原程序一致
    k.sort()
    if k.count(1) >= 1 or k.count(2) >= 2 or k.count(3) >= 3 or k == [2, 4, 4]:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    # 示例执行：可自行修改 n 的值
    main(3)