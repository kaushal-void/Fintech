def find_max_value(numbers):
    if not numbers:
        return None

    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value


print(find_max_value([10, 45, 23, 89, 67]))