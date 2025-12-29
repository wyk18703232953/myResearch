import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 这里生成 1~100 之间的随机整数，可按需修改
    lis = [random.randint(1, 100) for _ in range(n)]
    
    # 2. 原逻辑
    sor = sorted(lis)
    cnt = 0
    for i in range(n):
        if lis[i] != sor[i]:
            cnt += 1

    if cnt > 2:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)