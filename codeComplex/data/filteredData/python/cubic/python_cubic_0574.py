import random

def solve(a_str: str, b_str: str) -> int:
    a = [int(i) for i in list(a_str)]
    b = [int(i) for i in list(b_str)]

    if len(a) < len(b):
        a.sort(reverse=True)
        ans = 0
        for i in range(len(a)):
            ans = ans * 10 + a[i]
        return ans
    else:
        ans = 0
        n = len(a)
        count = [0] * 10
        for i in range(n):
            count[a[i]] += 1
        i = 0
        while i < n:
            x = b[i]
            if count[x] > 0:
                ans = ans * 10 + x
                count[x] -= 1
                i += 1
            else:
                break
        if i == n:
            return ans
        x = b[i]
        flag = False
        for j in range(x - 1, -1, -1):
            if count[j] > 0:
                ans = ans * 10 + j
                count[j] -= 1
                flag = True
                break
        if flag:
            for j in range(9, -1, -1):
                while count[j] > 0:
                    ans = ans * 10 + j
                    count[j] -= 1
        else:
            while not flag:
                t = ans % 10
                ans = ans // 10
                count[t] += 1
                for i in range(t - 1, -1, -1):
                    if count[i] > 0:
                        count[i] -= 1
                        flag = True
                        ans = ans * 10 + i
                        break
            for j in range(9, -1, -1):
                while count[j] > 0:
                    ans = ans * 10 + j
                    count[j] -= 1
        return ans


def main(n: int):
    """
    生成规模为 n 的测试数据并运行原逻辑。

    设：
      - a 的长度为 n
      - b 的长度在 1 到 n 之间随机
      - 数字内容为随机 0~9
    """
    if n <= 0:
        return

    # 生成随机 a、b
    a_len = n
    b_len = random.randint(1, n)

    a_digits = [str(random.randint(0, 9)) for _ in range(a_len)]
    b_digits = [str(random.randint(0, 9)) for _ in range(b_len)]

    a_str = "".join(a_digits)
    b_str = "".join(b_digits)

    ans = solve(a_str, b_str)
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)