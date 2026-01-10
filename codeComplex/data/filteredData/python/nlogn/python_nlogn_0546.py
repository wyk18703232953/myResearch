def main(n):
    # Generate deterministic input of size n
    # Original input: n, then list l of length n
    # Here we set l[i] = (i * 2 + 3) % (n + 7) + 1 to avoid too many zeros and keep it deterministic
    l = [((i * 2 + 3) % (n + 7)) + 1 for i in range(n)]

    index = list(range(1, n + 1))
    ans = [""] * n

    # Sort by l descending, keeping index
    paired = list(zip(l, index))
    paired.sort(reverse=True)
    l1, index1 = zip(*paired)

    for i in range(n):
        k = 1
        flag = False
        while (index1[i] - k * l1[i]) > 0:
            if l[index1[i] - k * l1[i] - 1] > l[index1[i] - 1]:
                if ans[index1[i] - k * l1[i] - 1] == "B":
                    ans[index1[i] - 1] = "A"
                    flag = True
                    break
            k += 1

        k = 1
        if not flag:
            while (index1[i] + k * l1[i]) <= n:
                if l[index1[i] + k * l1[i] - 1] > l[index1[i] - 1]:
                    if ans[index1[i] + k * l1[i] - 1] == "B":
                        ans[index1[i] - 1] = "A"
                        flag = True
                        break
                k += 1

        if not flag:
            ans[index1[i] - 1] = "B"

    print("".join(ans))


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)