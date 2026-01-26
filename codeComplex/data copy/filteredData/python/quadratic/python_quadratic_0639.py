def solve(n, a):
    a = sorted(a)
    col = [False for _ in range(n)]
    count = 0
    for i in range(n):
        if not col[i]:
            count += 1
            col[i] = True
            for j in range(n):
                if a[j] % a[i] == 0:
                    col[j] = True
    return count

def main(n):
    if n <= 0:
        return 0
    # 生成确定性的测试数据：a[i] = (i + 1) * 2
    a = [(i + 1) * 2 for i in range(n)]
    result = solve(n, a)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)