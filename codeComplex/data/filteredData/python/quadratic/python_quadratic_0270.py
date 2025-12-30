import random

def main(n: int):
    # 生成两个长度为 n 的列表，元素范围 1~2n
    list1 = [random.randint(1, 2 * n) for _ in range(n)]
    list2 = [random.randint(1, 2 * n) for _ in range(n)]

    # 输出 list1 中出现在 list2 中的元素（保持顺序）
    for i in list1:
        if i in list2:
            print(i, end=' ')

if __name__ == "__main__":
    # 示例调用，可按需要修改 n
    main(5)