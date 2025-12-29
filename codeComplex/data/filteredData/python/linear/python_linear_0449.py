import random
import string

def main(n: int):
    # 生成测试数据
    # 约束：|s| <= n, |t| <= n
    # 随机决定是否在 s 中放入 '*'
    has_star = random.choice([True, False])
    
    # 生成 s
    if has_star:
        # 确保 s 中有一个 '*'
        # 随机生成前后缀长度，总长不超过 n-1（加上一个 * 恰好不超过 n）
        max_len = max(1, n - 1)
        front_len = random.randint(0, max_len // 2)
        back_len = random.randint(0, max_len - front_len)
        front = ''.join(random.choices(string.ascii_lowercase, k=front_len))
        back = ''.join(random.choices(string.ascii_lowercase, k=back_len))
        s = front + "*" + back
    else:
        # 不含 '*' 的 s，长度不超过 n
        length = random.randint(0, n)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))

    # 生成 t：长度不超过 n
    t_len = random.randint(0, n)
    t = ''.join(random.choices(string.ascii_lowercase, k=t_len))

    # 原始逻辑
    if "*" in s:
        front, back = s.split("*")
        if len(t) >= len(s) - 1 and t.startswith(front) and t.endswith(back):
            print("YES")
        else:
            print("NO")
    else:
        print("YES" if s == t else "NO")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)