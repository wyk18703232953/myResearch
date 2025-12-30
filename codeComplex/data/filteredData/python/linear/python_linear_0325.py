import random
import string

def main(n: int):
    # 生成测试数据：
    # 生成 n 个“last”字符串和 n 个“current”字符串，
    # 两个列表中都会有部分重叠，部分不重叠
    # 字符串长度 5，字符集小写字母
    def rand_str(k=5):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(k))

    last = [rand_str() for _ in range(n)]
    current = [rand_str() for _ in range(n)]

    # 为了保证有交集，随机选若干位置使两边相同
    common_cnt = n // 3
    for i in range(common_cnt):
        val = rand_str()
        last[i] = val
        current[i] = val

    # 下面是原逻辑的实现
    last_copy = last[:]       # 不在原数据上修改，以防需要调试
    current_copy = current[:]

    for i in range(len(last_copy)):
        if last_copy[i] in current_copy:
            idx = current_copy.index(last_copy[i])
            current_copy[idx] = "*"
            last_copy[i] = "*"

    last_copy.sort()
    current_copy.sort()

    total = 0
    for i in range(len(last_copy)):
        if last_copy[i] == current_copy[i]:
            continue
        else:
            total += 1

    print(total)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)