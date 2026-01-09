def main(n):
    # Interpret n as the first input number; derive k deterministically from n
    # Example mapping: original input was "n k"
    # Here we set:
    #   N = n
    #   K = n // 2
    N = n
    K = n // 2

    result = N - int(((9 + 8 * (N + K)) ** 0.5 - 3) / 2)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)