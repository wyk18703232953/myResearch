import random

def main(n: int):
    # 3. 根据 n 生成测试数据（随机生成 n 个 1~10 的整数）
    ls = [random.randint(1, 10) for _ in range(n)]

    # 按原逻辑处理
    ls.sort()
    if ls.count(ls[0]) == len(ls):
        print('NO')
        return

    for x in ls:
        if x != ls[0]:
            print(x)
            break

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)