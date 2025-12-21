def main(n, k):
    data = list(range(1, n + 1))
    span = data[-1] - data[0]
    delta = [data[i + 1] - data[i] for i in range(n - 1)]
    delta.sort(reverse=True)
    return span - sum(delta[:k - 1])


if __name__ == "__main__":
    print(main(10, 3))