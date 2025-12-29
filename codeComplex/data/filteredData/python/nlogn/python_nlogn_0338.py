import random
import string


def main(n: int):
    # 1. 生成规模为 n 的测试数据（字符串列表）
    # 为了更容易满足“每个后面的字符串包含前面的字符串”这个条件，
    # 构造方式为：第 i+1 个字符串在第 i 个字符串基础上随机添加若干字符。
    ar = []
    # 生成第一个随机字符串
    length = random.randint(1, max(1, n // 2))
    s = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    ar.append(s)

    # 后续字符串在前一个字符串基础上扩展
    for _ in range(1, n):
        base = ar[-1]
        extra_len = random.randint(0, max(1, n // 2))
        extra = "".join(random.choice(string.ascii_lowercase) for _ in range(extra_len))
        # 随机在前一个字符串的任意位置插入额外字符
        pos = random.randint(0, len(base))
        new_s = base[:pos] + extra + base[pos:]
        ar.append(new_s)

    # 2. 原始逻辑：按长度排序，检查是否满足“每个字符串都是后一个字符串的子串”
    sortedAr = sorted(ar, key=len)
    flag = False
    for i in range(n - 1):
        if sortedAr[i + 1].find(sortedAr[i]) == -1:
            print("NO")
            flag = True
            break
    if not flag:
        print("YES")
        for s in sortedAr:
            print(s)


if __name__ == "__main__":
    # 示例：运行 main，规模可在此修改
    main(5)