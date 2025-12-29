import random
import string

def generate_random_string(length=5):
    # 生成一个由小写字母组成的随机字符串
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def main(n):
    # 根据规模 n 生成测试数据
    # 这里简单地生成两个长度为 n 的字符串列表
    l1 = [generate_random_string() for _ in range(n)]
    l2 = [generate_random_string() for _ in range(n)]

    # 原逻辑
    c = 0
    l2_copy = l2[:]  # 避免在调试或扩展时直接修改原始测试数据
    for i in range(n):
        if l1[i] in l2_copy:
            l2_copy.remove(l1[i])
        else:
            c += 1

    print(c)

if __name__ == "__main__":
    # 可自行修改 n 来测试不同规模
    main(10)