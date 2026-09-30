if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = (
            input().split()
        )  # first input part we call 'name', other all goes to 'line'
        scores = list(
            map(float, line)
        )  # make the entered strings (marks) in to floating numbers | String ---> float
        student_marks[name] = scores  # giving the made marks to the correct key of dic.

    query_name = input()

    # calculate the avg of given key value
    initial_scores = student_marks[query_name]
    average_marks = sum(initial_scores) / len(initial_scores)

    # print it with two decimal points
    print(f"{average_marks:.2f}")
