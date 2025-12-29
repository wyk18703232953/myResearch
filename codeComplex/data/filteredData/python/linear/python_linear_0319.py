import random
import string

def main(n: int):
    # 1. 随机生成 n 个字符串作为初始列表 a
    #   每个字符串长度在 3~8 之间，由小写字母组成
    a = [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
        for _ in range(n)
    ]

    # 2. 随机生成 n 个字符串作为“删除尝试”列表 queries
    #   一半概率从 a 中选一个（保证存在），一半概率随机生成（可能不存在）
    queries = []
    for _ in range(n):
        if a and random.random() < 0.5:
            # 从 a 中随机选一个已有元素
            queries.append(random.choice(a))
        else:
            # 随机生成一个字符串
            queries.append(
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
            )

    # 3. 模拟原程序逻辑
    for t in queries:
        if t in a:
            a.remove(t)

    # 4. 输出剩余元素数量
    print(len(a))


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)