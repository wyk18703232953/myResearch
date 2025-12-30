import random

def main(n: int):
    # 生成测试数据：4 个 n×n 的 01 字符矩阵，用字符串表示每一行
    lst1 = [[ "".join(random.choice("01") for _ in range(n)) ] for _ in range(n)]
    lst2 = [[ "".join(random.choice("01") for _ in range(n)) ] for _ in range(n)]
    lst3 = [[ "".join(random.choice("01") for _ in range(n)) ] for _ in range(n)]
    lst4 = [[ "".join(random.choice("01") for _ in range(n)) ] for _ in range(n)]

    ans_b1 = 0
    ans_w1 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst1[x][0][y] == '0':
                    ans_b1 += 1
                else:
                    ans_w1 += 1
            else:
                if lst1[x][0][y] == '1':
                    ans_b1 += 1
                else:
                    ans_w1 += 1

    ans_b2 = 0
    ans_w2 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst2[x][0][y] == '0':
                    ans_b2 += 1
                else:
                    ans_w2 += 1
            else:
                if lst2[x][0][y] == '1':
                    ans_b2 += 1
                else:
                    ans_w2 += 1

    ans_b3 = 0
    ans_w3 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst3[x][0][y] == '0':
                    ans_b3 += 1
                else:
                    ans_w3 += 1
            else:
                if lst3[x][0][y] == '1':
                    ans_b3 += 1
                else:
                    ans_w3 += 1

    ans_b4 = 0
    ans_w4 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst4[x][0][y] == '0':
                    ans_b4 += 1
                else:
                    ans_w4 += 1
            else:
                if lst4[x][0][y] == '1':
                    ans_b4 += 1
                else:
                    ans_w4 += 1

    result = (2 * n) ** 2 - max(
        ans_b1 + ans_b2 + ans_w3 + ans_w4,
        ans_b1 + ans_w2 + ans_b3 + ans_w4,
        ans_b1 + ans_w2 + ans_w3 + ans_b4,
        ans_w1 + ans_b2 + ans_b3 + ans_w4,
        ans_w1 + ans_b2 + ans_w3 + ans_b4,
        ans_w1 + ans_w2 + ans_b3 + ans_b4,
    )
    print(result)


if __name__ == "__main__":
    main(4)