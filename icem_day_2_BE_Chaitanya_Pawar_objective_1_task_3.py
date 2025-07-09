# Name: Chaitany Pawar

# Task 3 chain Filter(), map() and reduce() in one function
def process_numbers(numbers):
    filtered = filter(lambda n: n % 2 == 0, numbers)

    mapped = map(lambda n: n * 2, filtered)

    result = 0
    for num in mapped:
        result += num

    return result

nums = [1, 2, 3, 4, 5, 6]
result = process_numbers(nums)
print(result)
