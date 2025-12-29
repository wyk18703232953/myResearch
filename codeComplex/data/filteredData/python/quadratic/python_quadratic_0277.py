import random

def main(n):
    # 生成测试数据：seq 和 fp 各有 n 个元素，元素为 1..(2n) 间的随机整数（字符串形式）
    m = n
    universe = [str(i) for i in range(1, 2 * n + 1)]
    seq = random.sample(universe, n)
    fp = random.sample(universe, m)

    checklist = []
    for number in seq:
        if number in fp:
            checklist.append(number)

    print(" ".join(checklist))


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小
    main(5)