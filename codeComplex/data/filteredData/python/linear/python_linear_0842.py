import random
import string

def solve_case(n, k, s):
    rgb = "RGB"
    ans = n
    for i in range(3):
        r = [0]
        l = i
        for c in s:
            r.append(r[-1] + (1 if c != rgb[l] else 0))
            l = (l + 1) % 3
            if len(r) > k:
                ans = min(ans, r[-1] - r[len(r) - 1 - k])
    return ans

def main(n):
    # n 作为规模，这里用来生成测试数据：
    # 1. 令 q = n（生成 n 组测试）
    # 2. 对第 i 组测试：
    #    - 字符串长度 len(s) = n + i
    #    - k 在 [1, len(s)] 之间随机
    #    - s 为随机的 'R','G','B' 字符串
    q = n
    random.seed(0)
    results = []
    for i in range(q):
        length = n + i if n + i > 0 else 1
        k = random.randint(1, length)
        s = ''.join(random.choice("RGB") for _ in range(length))
        ans = solve_case(length, k, s)
        results.append(ans)
    # 输出所有测试的答案，每行一个
    for ans in results:
        print(ans)

if __name__ == "__main__":
    # 示例：可修改这里的 n 来控制规模
    main(5)