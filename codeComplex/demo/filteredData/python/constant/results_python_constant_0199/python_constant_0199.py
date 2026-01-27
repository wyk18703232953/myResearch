def main(n):
    # Generate deterministic input list of length 3 based on n
    # Ensure values are positive and varied but deterministic
    l = [n % 5 + 1, (n * 2) % 5 + 1, (n * 3) % 5 + 1]
    l = sorted(l)
    if min(l) == 1 or (l[0] == 3 and l[1] == 3 and l[2] == 3) or (l[0] == 2 and l[1] == 4 and l[2] == 4) or (l[0] == 2 and l[1] == 2):
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(10)