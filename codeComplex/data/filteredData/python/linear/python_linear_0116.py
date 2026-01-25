import math

def main(n):
    result = (math.floor(n / 2) + 1) * math.ceil(n / 2)
    print(result)

if __name__ == "__main__":
    main(10)