def main(n):
    ans = 1
    for i in range(n):
        ans += i * 4
    print(ans)


if __name__ == "__main__":
    main(10)