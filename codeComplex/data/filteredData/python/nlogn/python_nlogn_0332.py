import random
import string

def generate_test_data(n):
    """
    生成满足/不满足原始逻辑的测试数据：
    - 约一半概率生成满足条件的用例（YES）
    - 约一半概率生成不满足条件的用例（NO）
    """
    words = []

    # 随机决定是否生成一定满足 YES 的数据
    force_yes = random.choice([True, False])

    if force_yes:
        # 生成一条基础字符串
        base_len = random.randint(1, 5)
        base = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))
        words.append(base)

        # 后续每个字符串都是在前一个基础上随机插入字符，保证前者是后者子串
        for _ in range(n - 1):
            prev = words[-1]
            # 将 prev 插入到一个随机噪声字符串中，保证 prev 是子串
            noise_len = random.randint(0, 3)
            noise_left = ''.join(random.choice(string.ascii_lowercase) for _ in range(noise_len))
            noise_right = ''.join(random.choice(string.ascii_lowercase) for _ in range(noise_len))
            new_word = noise_left + prev + noise_right
            words.append(new_word)
    else:
        # 普通随机字符串，不保证 YES
        for _ in range(n):
            length = random.randint(1, 10)
            s = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
            words.append(s)

    return words


def main(n):
    # 生成测试数据
    words = generate_test_data(n)

    # 将原逻辑封装到 main 中
    l = []
    nn = n

    for s in words:
        l.append([len(s), s])

    l.sort()  # 按长度排序（len在前，字符串在后）

    ch = 1
    ans = []

    for i in range(nn - 1):
        if l[i][1] not in l[i + 1][1]:
            ch = 0
            break
        else:
            ans.append(l[i][1])

    if ch:
        ans.append(l[nn - 1][1])
        print("YES")
        print(*ans, sep="\n")
    else:
        print("NO")


# 示例调用：
# main(5)