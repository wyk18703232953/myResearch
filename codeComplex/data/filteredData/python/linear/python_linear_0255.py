import random
import string

def generate_test_data(n: int) -> str:
    # 随机生成长度为 n 的字符串，字符集为小写字母
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def main(n: int) -> int:
    s = generate_test_data(n)

    while s != "":
        if s == s[::-1]:
            s = s[:len(s) - 1]
        else:
            break

    # 返回结果而不是打印，方便在测试框架中使用
    return len(s)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改
    result = main(10)
    print(result)