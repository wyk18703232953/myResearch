def main(n):
    a = [i % (n // 2 + 1) for i in range(n)]
    c = 0
    for i in range(n):
        if a[i] > c:
            # print(i + 1)
            pass
            break

        else:
            c = max(a[i] + 1, c)

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)