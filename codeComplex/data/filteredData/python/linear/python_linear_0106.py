import random
import string

def main(n: int):
    # 1. 生成测试数据：两个小写字母字符串 s1, s2，长度由 n 控制
    #    这里约定：s1 长度为 n，s2 长度为 1（保持原逻辑语义清晰）
    if n <= 0:
        return ""

    # 生成 s1：长度为 n 的随机小写字母串
    s1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    # 生成 s2：长度为 1 的随机小写字母串
    s2 = random.choice(string.ascii_lowercase)

    # 2. 原始逻辑
    ans = s1[0]
    for i in range(1, len(s1)):
        if s1[i] < s2[0]:
            ans += s1[i]
        else:
            break

    result = ans + s2[0]
    print(result)
    return result

if __name__ == "__main__":
    # 示例运行：可根据需要调整 n
    main(10)