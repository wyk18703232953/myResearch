import random

def solve(a: str, b: str) -> str:
    la = [int(x) for x in a]
    res = []
    la.sort()
    la = la[::-1]
    lb = [int(x) for x in b]
    cnt = [0] * 20

    def check() -> bool:
        tres = 0
        for x in range(len(res)):
            tres *= 10
            tres += int(res[x])
        return tres <= int(b)

    if len(a) < len(b):
        return ''.join(str(x) for x in la)
    else:
        for i in range(len(la)):
            cnt[la[i]] += 1
        flag = 0
        for i in range(len(lb)):
            if flag == 0 and cnt[lb[i]]:
                res.append(lb[i])
                cnt[lb[i]] -= 1
            else:
                flag = i - 1
                for j in range(lb[i] - 1, -1, -1):
                    if cnt[j]:
                        res.append(j)
                        cnt[j] -= 1
                        break
                for j in range(9, -1, -1):
                    while cnt[j]:
                        res.append(j)
                        cnt[j] -= 1
                break
        while not check():
            temp = []
            cnt = [0] * 20
            for x in range(flag):
                temp.append(res[x])
                cnt[res[x]] -= 1
            for i in la:
                cnt[i] += 1
            res = temp
            for v in range(lb[flag] - 1, -1, -1):
                if cnt[v]:
                    res.append(v)
                    cnt[v] -= 1
                    break
            for v in range(9, -1, -1):
                while cnt[v]:
                    res.append(v)
                    cnt[v] -= 1
            flag -= 1
        return ''.join(str(x) for x in res)

def main(n: int):
    # 生成规模为 n 的测试数据：
    # a 为长度 n 的随机数字串，首位不为 0
    # b 为长度在 [1, n] 之间的随机数字串，首位不为 0
    if n <= 0:
        return

    def rand_number(length: int) -> str:
        if length == 1:
            return str(random.randint(0, 9))
        first = str(random.randint(1, 9))
        rest = ''.join(str(random.randint(0, 9)) for _ in range(length - 1))
        return first + rest

    len_a = n
    len_b = random.randint(1, n)
    a = rand_number(len_a)
    b = rand_number(len_b)

    ans = solve(a, b)
    print(ans)

if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)