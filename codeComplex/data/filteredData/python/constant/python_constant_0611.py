def main(n):
    # Interpret n as the number of test cases
    t = n

    # Deterministically generate t pairs (l, r)
    # Example scheme: l = i+1, r = (i+1)*2
    queries = [(i + 1, (i + 1) * 2) for i in range(t)]

    results = []
    for l, r in queries:
        l -= 1
        sr = r // 2 + (r % 2) * -r
        sl = l // 2 + (l % 2) * -l
        results.append(sr - sl)

    # Keep printing behavior for observability / timing
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)