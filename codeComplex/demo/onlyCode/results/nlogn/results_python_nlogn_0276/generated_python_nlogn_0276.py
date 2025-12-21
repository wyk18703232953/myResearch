def main(n):
    ans = {}
    for i in range(1, n + 1):
        a = i
        b = i * 2
        ans[a] = b
    for i in range(1, n + 1):
        a = i
        b = i * 3
        if a in ans:
            ans[a] = max(ans[a], b)
        else:
            ans[a] = b
    return sum(ans.values())


if __name__ == "__main__":
    print(main(10))