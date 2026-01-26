def main(n):
    # For deterministic data generation, we interpret n as:
    # - number of students
    # - each student has k subjects, here choose k = 3
    k = 3
    # First student's scores: simple arithmetic progression
    first_student_scores = [i % 10 + 1 for i in range(k)]
    score = sum(first_student_scores)

    rank = 1
    # Generate scores for remaining n-1 students deterministically
    for i in range(1, n):
        # Each student i has k scores based on i and subject index j
        student_scores = [(i + j) % 10 + 1 for j in range(k)]
        student_sum = sum(student_scores)
        if student_sum > score:
            rank += 1

    # print(rank)
    pass
    return rank

if __name__ == "__main__":
    main(5)