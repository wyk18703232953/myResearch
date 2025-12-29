import random
import string

def main(n: int):
    # 1. 生成测试数据：两个长度为 n 的小写字母字符串 first, last
    #   可根据需要调整生成规则，这里简单用随机小写字母
    if n <= 0:
        return  # 没有意义的规模，直接返回

    def random_str(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    first = random_str(n)
    last = random_str(n)

    # 2. 原逻辑
    username = first[0]
    first_rest = first[1:]
    while first_rest != "" and first_rest[0] < last[0]:
        username += first_rest[0]
        first_rest = first_rest[1:]
    result = username + last[0]

    # 输出结果（可根据需要额外输出测试数据）
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时由外部指定 n
    main(5)