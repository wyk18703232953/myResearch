def main(n):
    answer = 0
    for i in range(1, 2 * n - 2, 2):
        answer += i
    result = answer * 2 + 2 * n - 1
    print(result)
    return result

if __name__ == "__main__":
    main(10)