def main(n):
    # Interpret n as the number of test cases
    results = []
    for k in range(1, n + 1):
        ax, ay = k, k + 1
        bx, by = k + 2, k + 3
        cx, cy = k + 4, k + 5

        if (bx > ax, by > ay) != (cx > ax, cy > ay):
            results.append("NO")

        else:
            results.append("YES")
    # For time complexity experiments, we can print the last result
    # or join all if needed; here we print all to keep behavior visible.
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)