import random
import string

def generate_test_data(n: int):
    """
    生成 n 个字符串测试数据。
    保证长度大致递增，且后面的字符串有一定概率包含前面的字符串，
    以更贴合原程序的逻辑场景。
    """
    if n <= 0:
        return []

    random.seed(0)  # 固定种子，方便复现
    strings = []

    # 基础字符串长度范围
    min_len = 1
    max_len = 10

    for i in range(n):
        # 随着 i 增大，字符串期望长度略有增加
        length = random.randint(min_len, max_len + i // 3)
        if i > 0 and random.random() < 0.7:
            # 70% 概率构造一个包含前面某个字符串的串
            base = random.choice(strings)
            extra_len = max(0, length - len(base))
            extra = ''.join(random.choices(string.ascii_lowercase, k=extra_len))
            # 将 base 插入到 extra 的某个位置
            pos = random.randint(0, len(extra))
            s = extra[:pos] + base + extra[pos:]
        else:
            # 随机字符串
            s = ''.join(random.choices(string.ascii_lowercase, k=length))
        strings.append(s)

    return strings

def main(n: int):
    # 1. 生成测试数据（代替原来的 input 读入）
    ar = generate_test_data(n)

    # 2. 原算法逻辑
    sortedAr = sorted(ar, key=len)
    flag = False
    for i in range(n - 1):
        if sortedAr[i + 1].find(sortedAr[i]) == -1:
            print('NO')
            flag = True
            break
    if not flag:
        print('YES')
        for s in sortedAr:
            print(s)

if __name__ == "__main__":
    # 示例：可以在此修改 n 测试
    main(5)