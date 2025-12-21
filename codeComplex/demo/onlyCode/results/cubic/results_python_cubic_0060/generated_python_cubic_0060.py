def main(n):
    name = "a" * n
    for i in range(len(name), 0, -1):
        for j in range(len(name) - i + 1):
            if name[j: j + i] in name[j + 1:]:
                return i
    return 0

if __name__ == "__main__":
    print(main(10))