import random
import string

def main(n: int):
    # 根据规模 n 生成测试数据：两个长度为 n 的随机小写字母串
    def random_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    s1 = random_string(n)
    s2 = random_string(n)

    ans = 'z' * 21
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            candidate = s1[:i] + s2[:j]
            if candidate < ans:
                ans = candidate

    print(ans)


if __name__ == "__main__":
    # 示例：可在此处修改规模 n
    main(5)