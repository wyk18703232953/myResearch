import random
import string

def main(n: int):
    # 1. 生成测试数据：构造一个字符串列表 lis，共 n 个字符串
    # 规则：生成一个基础字符串，然后后面的字符串尽量包含前面的，模拟原逻辑的典型 YES 情况
    lis = []
    base = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
    lis.append(base)
    for _ in range(1, n):
        # 在已有字符串中随机选择一个作为子串，然后随机添加前后缀
        sub = random.choice(lis)
        prefix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(0, 3)))
        suffix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(0, 3)))
        lis.append(prefix + sub + suffix)

    # 2. 按长度排序
    lis = sorted(lis, key=len)

    # 3. 检查每个字符串是否为下一个字符串的子串
    for i in range(len(lis) - 1):
        if lis[i] not in lis[i + 1]:
            print("NO")
            return

    # 4. 若都满足条件，输出 YES 和字符串列表
    print("YES")
    for s in lis:
        print(s)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)