def solution(dartResult):
    import itertools
    input_list = ["".join(x) for _, x in itertools.groupby(dartResult, key=str.isdigit)]
    a = list()
    for idx, letter in enumerate(input_list):
        if letter.isdigit() and idx < len(input_list):
            a.append([int(letter), input_list[idx + 1]])

    for idx, i in enumerate(a):
        score, bonus = i[0], i[1]
        if "D" in bonus:
            a[idx][0] = a[idx][0] ** 2
        elif "T" in bonus:
            a[idx][0] = a[idx][0] ** 3

        if "*" in bonus:
            a[idx][0] = a[idx][0] * 2
            if idx >= 1:
                a[idx - 1][0] = a[idx - 1][0] * 2
        elif "#" in bonus:
            a[idx][0] = (-1) * a[idx][0]

    return sum([x[0] for x in a])


print(solution('1D2S3T*'))
