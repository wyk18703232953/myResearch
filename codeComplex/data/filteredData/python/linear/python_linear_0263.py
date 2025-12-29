import random
import string


def generate_test_string(n: int) -> str:
    """
    根据规模 n 生成测试字符串：
    - n <= 0 时返回空串
    - 否则生成长度为 n 的随机小写字母串
    """
    if n <= 0:
        return ""
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def main(n: int):
    # 1. 根据 n 生成测试数据（字符串 s）
    s = generate_test_string(n)

    # 2. 按原逻辑处理字符串并输出结果
    while True:
        if len(s) == 1:
            print(0)
            break
        elif s == s[::-1]:
            s = s[1:]
        else:
            print(len(s))
            break


if __name__ == "__main__":
    # 示例：可以在这里手动指定 n 进行测试
    main(10)