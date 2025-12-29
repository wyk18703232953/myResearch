import random

def find(moves, candiesAtTheEnd):
    start = 0
    end = moves - 1
    while True:
        mid = (end - start + 1) // 2 + start
        pluses = moves - mid
        minuses = mid

        # 原公式中使用的是 /，在 Python3 中会变成 float，改为整型等价形式：
        # ((pluses + 1) / 2) * pluses = (pluses * (pluses + 1)) // 2
        result = (pluses * (pluses + 1)) // 2 - minuses

        if result == candiesAtTheEnd:
            return minuses
        elif result > candiesAtTheEnd:
            start = mid
        else:
            end = mid

def main(n):
    # 根据规模 n 生成测试数据
    # 这里将 moves 设为 n，candiesAtTheEnd 在 [0, n*(n+1)//2] 范围内随机生成
    moves = n
    max_candies = moves * (moves + 1) // 2
    candiesAtTheEnd = random.randint(0, max_candies)

    result_final = find(moves, candiesAtTheEnd)
    print("moves:", moves)
    print("candiesAtTheEnd:", candiesAtTheEnd)
    print("result:", result_final)

if __name__ == "__main__":
    # 举例运行：n = 10
    main(10)