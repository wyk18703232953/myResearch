import copy
import random

def generate_matrix(n):
    # 随机生成一个 n×n 的由 '.' 和 '#' 构成的矩阵（行是 tuple）
    return [tuple(random.choice(".#") for _ in range(n)) for _ in range(n)]

def is_rotated_equal(mat1, mat2, n):
    mats = []
    mats.append(mat2)

    matu = copy.copy(mat2)
    matv = copy.copy(mat2)
    matv = list(zip(*matv))
    mats.append(matv)

    mattem = copy.copy(matu)
    for _ in range(3):
        mattem = list(zip(*list(reversed(mattem))))
        mats.append(mattem)

    mattem = copy.copy(matv)
    for _ in range(3):
        mattem = list(zip(*list(reversed(mattem))))
        mats.append(mattem)

    flg = 0
    for cmat in mats:
        flg2 = 1
        for ri in range(0, n):
            if cmat[ri] != mat1[ri]:
                flg2 = 0
                break
        if flg2 == 1:
            flg = 1
            break
    return flg == 1

def main(n):
    # 生成测试数据
    mat1 = generate_matrix(n)

    # 随机选择是否生成一个与 mat1 旋转相关的 mat2，便于覆盖 Yes/No 两种情况
    if random.choice([True, False]):
        # 生成一个随机旋转版本作为 mat2，让结果更可能为 Yes
        mat2 = mat1
        # 进行 0~7 次旋转操作，复用原逻辑中的旋转方式
        mat2_list = list(mat2)
        for _ in range(random.randint(0, 7)):
            mat2_list = list(zip(*list(reversed(mat2_list))))
        mat2 = [tuple(row) for row in mat2_list]
    else:
        # 完全随机的 mat2，更可能为 No
        mat2 = generate_matrix(n)

    if is_rotated_equal(mat1, mat2, n):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    # 示例：规模为 5，可按需修改
    main(5)