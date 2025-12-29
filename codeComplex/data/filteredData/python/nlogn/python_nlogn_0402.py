import random

bo = 10 ** 6

coef = [
    [1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
    [1, 0, 1], [1, 0, -1], [-1, 0, 1], [-1, 0, -1],
    [0, 1, 1], [0, 1, -1], [0, -1, 1], [0, -1, -1]
]


def lv(x):
    return (x[0] ** 2 + x[1] ** 2) ** 0.5


def main(n: int):
    # 根据 n 生成测试数据 vec，保持与原程序输入格式一致
    # 这里生成 n 个二维向量，每个分量在 [-1000, 1000] 内
    vec = [[random.randint(-1000, 1000), random.randint(-1000, 1000)] for _ in range(n)]

    if n == 1:
        res = [1]
    elif n == 2:
        if vec[0][0] * vec[1][0] + vec[0][1] * vec[1][1] <= 0:
            res = [1, 1]
        else:
            res = [1, -1]
    else:
        res = [0 for _ in range(n)]
        fer = [[vec[0], vec[1], vec[2]], [[0], [1], [2]]]
        for l in range(len(vec) - 2):
            for j in coef:
                der = [0, 0]
                der[0] = j[0] * fer[0][0][0] + j[1] * fer[0][1][0] + j[2] * fer[0][2][0]
                der[1] = j[0] * fer[0][0][1] + j[1] * fer[0][1][1] + j[2] * fer[0][2][1]
                if lv(der) <= bo:
                    ner = []
                    for i in range(3):
                        if j[i] != 0:
                            ner.append(i)
                    if len(fer[1][ner[0]]) == 1:
                        res[fer[1][ner[0]][0]] = j[ner[0]]
                    elif j[ner[0]] == -1:
                        for k in fer[1][ner[0]]:
                            res[k] *= -1
                    fer[0][ner[0]] = der
                    fer[1][ner[0]] += fer[1][ner[1]]
                    if len(fer[1][ner[1]]) == 1:
                        res[fer[1][ner[1]][0]] = j[ner[1]]
                    elif j[ner[1]] == -1:
                        for k in fer[1][ner[1]]:
                            res[k] *= -1
                    if l == len(vec) - 3:
                        del fer[0][ner[1]]
                        del fer[1][ner[1]]
                    else:
                        fer[0][ner[1]] = vec[3 + l]
                        fer[1][ner[1]] = [3 + l]
                    break
        if n >= 3:
            if fer[0][0][0] * fer[0][1][0] + fer[0][0][1] * fer[0][1][1] <= 0:
                if len(fer[1][0]) == 1:
                    res[fer[1][0][0]] = 1
                if len(fer[1][1]) == 1:
                    res[fer[1][1][0]] = 1
            else:
                if len(fer[1][0]) == 1:
                    res[fer[1][0][0]] = -1
                elif len(fer[1][1]) == 1:
                    res[fer[1][1][0]] = -1
                else:
                    for k in fer[1][0]:
                        res[k] *= -1

    res1 = ''
    for i in res:
        res1 += str(i) + ' '
    res1 = res1[:-1]
    print(res1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)