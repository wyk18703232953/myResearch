import random
from math import sqrt

def main(n: int):
    # 1. 生成测试数据：长度为 n 的 0/1 列表（模拟原代码的数字串）
    #   这里用等概率生成 0 和 1，你可以按需要调整分布
    l = [random.randint(0, 1) for _ in range(n)]

    # 2. 保留原 solve 的核心逻辑，只是去掉 input，改用生成的 l
    divisors = []
    total = sum(l)

    for j in range(2, int(sqrt(total)) + 1):
        if total % j == 0:
            divisors.extend([j, total // j])

    if total == 0:
        print("YES")
        return

    if total != 1:
        divisors.append(1)

    for x in divisors:
        search = x
        index = 0
        summ = 0
        while index < n:
            summ += l[index]
            if summ > search:
                break
            elif summ == search:
                summ = 0
            index += 1

        if summ == 0 and index == n:
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可自行修改 n
    main(10)