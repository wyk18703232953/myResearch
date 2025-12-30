import random
import string

def generate_test_data(n: int) -> str:
    """
    根据规模 n 生成测试数据串：
    - 一半概率生成全是同一字符（典型极端回文情况）
    - 一半概率生成随机字符串
    """
    if n <= 0:
        return ""
    if random.random() < 0.5:
        # 全同字符
        ch = random.choice(string.ascii_lowercase)
        return ch * n
    else:
        # 随机字符串
        return ''.join(random.choices(string.ascii_lowercase, k=n))

def main(n: int) -> int:
    # 生成测试数据
    s = generate_test_data(n)

    # 原逻辑
    while len(s) > 0:
        if s != s[::-1]:
            break
        else:
            s = s[1:]

    # 输出结果（保留原程序行为：打印最终字符串长度）
    print(len(s))
    return len(s)

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)