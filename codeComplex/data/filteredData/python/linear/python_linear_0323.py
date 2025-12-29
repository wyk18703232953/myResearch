import random
import string

def main(n: int) -> int:
    # 生成测试数据：list1 中有 n 个字符串，每个长度 5
    list1 = [
        ''.join(random.choices(string.ascii_lowercase, k=5))
        for _ in range(n)
    ]

    # 第二批数据：从 list1 中随机选一些，再加上一些随机新字符串
    # 保证规模也是 n
    num_from_list1 = random.randint(0, n)
    second_list = []

    # 从 list1 中选 num_from_list1 个（允许重复）
    for _ in range(num_from_list1):
        second_list.append(random.choice(list1))

    # 其余用新字符串填充
    for _ in range(n - num_from_list1):
        second_list.append(
            ''.join(random.choices(string.ascii_lowercase, k=5))
        )

    # 按原逻辑处理
    for value in second_list:
        if value in list1:
            list1.remove(value)

    # 输出与返回剩余元素个数
    result = len(list1)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)