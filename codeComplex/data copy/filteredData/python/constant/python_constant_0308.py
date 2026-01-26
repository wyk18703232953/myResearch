def main(n):
    # Deterministically generate k, s, p from n
    k = n + 1
    s = max(1, n % 10 + 1)
    p = max(1, (n // 2) % 10 + 1)

    paper_person = (n + s - 1) // s
    total_needed = paper_person * k
    ans = (total_needed + p - 1) // p
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)