def main(n):
    # Generate deterministic input array of size n
    # Using simple arithmetic pattern: a[i] = i + 1
    a = [i + 1 for i in range(n)]
    a.sort()
    ans = 0
    for i in range(n):
        f = 1
        for j in range(i):
            if a[i] % a[j] == 0:
                f = 0
                break
        ans += f
    # print(ans)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)