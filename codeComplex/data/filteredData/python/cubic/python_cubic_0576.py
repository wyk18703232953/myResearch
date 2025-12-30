import random
import string

def solve_with_limit(a: str, b: str) -> str:
    if len(a) < len(b):
        a_list = list(a)
        a_list.sort(reverse=True)
        return ''.join(a_list)

    def solve(i, a_list: list):
        if i == len(b):
            return ''
        if b[i] in a_list:
            a_list.remove(b[i])
            suf = solve(i + 1, a_list)
            if suf is not None:
                return b[i] + suf
            a_list.append(b[i])
        best = ''
        for c in a_list:
            if c < b[i] and c > best:
                best = c
        if best == '':
            return None
        a_list.remove(best)
        a_list.sort(reverse=True)
        return best + ''.join(a_list)

    a_list = list(a)
    res = solve(0, a_list)
    return res if res is not None else ''

def main(n: int):
    # 生成测试数据：
    # 对于给定规模 n：
    # - b 的长度为 n
    # - a 的长度在 [1, n] 或 [n, 2n] 中随机，保证多样性
    # - 字符为数字字符，便于和原逻辑匹配（比较大小）
    if n <= 0:
        return

    # 决定 a 的长度
    if random.random() < 0.5:
        len_a = random.randint(1, n)
    else:
        len_a = random.randint(max(1, n), max(1, 2 * n))

    len_b = n

    digits = string.digits

    # a 和 b 由数字随机组成
    a = ''.join(random.choice(digits) for _ in range(len_a))
    b = ''.join(random.choice(digits) for _ in range(len_b))

    ans = solve_with_limit(a, b)
    print(ans)

if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(5)