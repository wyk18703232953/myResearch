import random
import string

def main(n: int):
    # 生成随机地图，元素为 '.' 或 '#'
    choices = ['.', '#']
    map_2 = [[random.choice(choices) for _ in range(n)] for _ in range(n)]

    # 随机选择一种变换生成 map_1，以保证有一定概率为 "Yes"
    transform_index = random.randint(0, 7)

    maps = []
    maps.append([[map_2[i][j] for j in range(n)] for i in range(n)])
    maps.append([[map_2[i][n - 1 - j] for j in range(n)] for i in range(n)])
    maps.append([[map_2[n - 1 - i][j] for j in range(n)] for i in range(n)])
    maps.append([[map_2[n - 1 - i][n - 1 - j] for j in range(n)] for i in range(n)])
    maps.append([[map_2[j][i] for j in range(n)] for i in range(n)])
    maps.append([[map_2[j][n - 1 - i] for j in range(n)] for i in range(n)])
    maps.append([[map_2[n - 1 - j][i] for j in range(n)] for i in range(n)])
    maps.append([[map_2[n - 1 - j][n - 1 - i] for j in range(n)] for i in range(n)])

    map_1 = maps[transform_index]

    print(('No', 'Yes')[any(map_1 == el for el in maps)])


if __name__ == "__main__":
    # 示例：n = 5
    main(5)