import random

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的列表，元素在 [1, n] 范围内
    # 注意：原逻辑中使用 lst.index(p)，要求列表中还至少有一个与 p 相同的元素
    # 为保证这一点，这里简单生成每个值两次（若 n 为奇数，最后一个值只出现一次会导致出错）
    # 因此对奇数 n 做一下调整，使用偶数长度 2 * (n // 2)
    length = 2 * (n // 2)
    if length == 0:
        return 0
    # 生成 [1, length // 2] 中的每个数各两次，然后打乱顺序
    base_vals = list(range(1, length // 2 + 1))
    lst = base_vals * 2
    random.shuffle(lst)

    c = 0
    # 按原程序逻辑处理
    while len(lst) != 0:
        p = lst[0]
        del lst[0]
        i = lst.index(p)
        c += i
        del lst[i]
    return c


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    result = main(10)
    print(result)