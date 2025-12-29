import random

def rotate_90(matrix):
    # Rotate matrix 90 degrees clockwise
    return [list(row) for row in zip(*matrix[::-1])]

def flip(matrix):
    # Flip matrix vertically
    return matrix[::-1]

def compare_matrices(first, second):
    n = len(first)
    for i in range(n):
        for j in range(n):
            if first[i][j] != second[i][j]:
                return False
    return True

def wrap(first, second):
    if compare_matrices(first, second):
        return 'Yes'
    hold_first = [row[:] for row in first]
    for _ in range(3):
        first = rotate_90(first)
        if compare_matrices(first, second):
            return 'Yes'
    first = hold_first
    first = flip(first)
    if compare_matrices(first, second):
        return 'Yes'
    for _ in range(3):
        first = rotate_90(first)
        if compare_matrices(first, second):
            return 'Yes'
    return 'No'

def main(n):
    # 根据 n 生成测试数据：随机生成第一个矩阵，然后对其进行随机旋转/翻转得到第二个矩阵
    chars = ['.', '#']
    first = [[random.choice(chars) for _ in range(n)] for _ in range(n)]

    # 生成 second：从 first 派生（保持 Yes/No 情况都可能）
    second = [row[:] for row in first]

    # 随机决定是否从 first 派生一个等价矩阵，或者生成完全随机的不同矩阵
    if random.random() < 0.7:
        # 70% 概率使 second 与 first 通过旋转/翻转等价
        # 随机执行一次翻转与若干次旋转
        if random.random() < 0.5:
            second = flip(second)
        k = random.randint(0, 3)
        for _ in range(k):
            second = rotate_90(second)
    else:
        # 30% 概率使 second 完全随机，通常不会等价
        second = [[random.choice(chars) for _ in range(n)] for _ in range(n)]

    result = wrap(first, second)
    print(result)

if __name__ == "__main__":
    # 示例：n = 4，可自行修改
    main(4)