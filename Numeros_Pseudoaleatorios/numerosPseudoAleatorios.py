import numpy as np
import math


def process_params(data):
    processed_params = data.split()
    return [int(num) for num in processed_params]


def next_random_number(a, c, m, x):
    return np.mod((a * x + c), m)


def solve(index, params_array):
    a = params_array[0]
    c = params_array[1]
    m = params_array[2]
    x = params_array[3]

    total_sum = 0
    even = 0
    odd = 0
    numbers = set()

    while x not in numbers:
        total_sum += x
        numbers.add(x)
        x = next_random_number(a, c, m, x)
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    period = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total_sum / len(numbers)
    case = "Caso " + str(index) + ":"

    squared_diffs = [(x - average) ** 2 for x in numbers]
    variance = sum(squared_diffs) / len(numbers)
    deviation = math.sqrt(variance)

    formatted_average = "{:.4f}".format(round(average, 4))
    formatted_variance = "{:.4f}".format(round(variance, 4))
    formatted_deviation = "{:.4f}".format(round(deviation, 4))

    print(case, period, formatted_average, formatted_variance, formatted_deviation, minimum, maximum, even, odd)


i = 1
while True:
    line = input()
    if line == "0 0 0 0":
        break
    params = process_params(line)
    solve(i, params)
    i += 1
