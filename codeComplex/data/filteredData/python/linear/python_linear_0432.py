rank = 1

def main(n):
    score = sum(i % 10 for i in range(3))
    rank = 1
    for i in range(n - 1):
        student = sum((i + j) % 10 for j in range(3))
        if student > score:
            rank += 1
    # print(rank)
    pass
if __name__ == "__main__":
    main(5)