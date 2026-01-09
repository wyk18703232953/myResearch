def main(n):
    # Deterministically generate a string of length n over lowercase letters
    # example pattern: repeating 'abcdefghijklmnopqrstuvwxyz'
    base = "abcdefghijklmnopqrstuvwxyz"
    string = "".join(base[i % 26] for i in range(n))

    maxi = 0
    for x in range(len(string)):
        substring = ""
        suffix = string[x:]
        for y in suffix:
            substring += y
            if suffix.rfind(substring) != suffix.find(substring):
                maxi = max(maxi, len(substring))
                continue
    # print(maxi)
    pass
if __name__ == "__main__":
    main(1000)