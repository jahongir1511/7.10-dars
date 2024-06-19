#misol linki   https://www.codewars.com/kata/5a005f4fba2a14897f000086/train/python


def sum_it_up(numbers):
    total_sum = 0

    for num_str, base in numbers:
        num_base_10 = int(num_str, base)
        total_sum += num_base_10

    return total_sum
