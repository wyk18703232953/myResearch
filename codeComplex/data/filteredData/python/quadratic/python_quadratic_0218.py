def main(n):
    m = n
    a = []
    for i in range(n):
        row = ''.join('1' if (i + j) % 3 == 0 else '0' for j in range(m))
        a.append(row)
    ans = "NO"
    count = [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] == '1':
                count[j] += 1
    for i in range(n):
        ans = "YES"
        for j in range(m):
            if count[j] == 1 and a[i][j] == '1':
                ans = "NO"
                break
        if ans == "YES":
            break
    print(ans)

if __name__ == "__main__":
    main(5)