import random

def main(n):
    # 生成测试数据 E：从 1~n 中随机取 n 个整数
    E = [random.randint(1, n) for _ in range(n)]
    
    D = {}
    for e in E:
        D[e] = D.get(e, 0) + 1
    for e in E:
        print(D[e])

if __name__ == "__main__":
    # 可在此处调整规模 n
    main(10)