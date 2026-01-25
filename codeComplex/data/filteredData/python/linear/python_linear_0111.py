def main(n):
    upper = n
    return sum(i for i in range(upper, -1, -2))

if __name__ == "__main__":
    print(main(10))