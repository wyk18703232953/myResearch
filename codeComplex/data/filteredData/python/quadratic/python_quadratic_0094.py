import random
import string

def main(n):
    # 生成随机测试数据矩阵 m2
    # 元素为 '0' 或 '1' 的 n x n 矩阵（字符串列表）
    m2 = [
        ''.join(random.choice('01') for _ in range(n))
        for _ in range(n)
    ]

    # 为了测试等价性，有一定概率让 m1 为 m2 的某种变换
    # 否则 m1 为完全随机矩阵
    def all_transforms(matrix):
        # 根据原逻辑生成所有可能的变换
        ms = [
            matrix,
            [x[::-1] for x in matrix],
            [x for x in reversed(matrix)],
        ]

        a = []
        for m in ms:
            a.append(m)
            a.append([x[::-1] for x in reversed(m)])
            a.append([''.join(m[j][i] for j in range(n - 1, -1, -1)) for i in range(n)])
            a.append([''.join(m[j][i] for j in range(n)) for i in range(n - 1, -1, -1)])
        return a

    transforms = all_transforms(m2)
    use_transform = random.choice([True, False])

    if use_transform:
        # 从所有变换中随机选择一个作为 m1
        m1 = random.choice(transforms)
    else:
        # 完全随机 m1
        m1 = [
            ''.join(random.choice('01') for _ in range(n))
            for _ in range(n)
        ]

    # 原逻辑判断
    ms = transforms
    result = ['NO', 'YES'][m1 in ms]
    print(result)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)