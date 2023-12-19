def get_user_numbers():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    return [int(num) for num in numbers]

def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

user_numbers = get_user_numbers()
print("Sum:", find_sum(user_numbers))
print("Average:", find_average(user_numbers))
print("Maximum:", find_maximum(user_numbers))
print("Minimum:", find_minimum(user_numbers))
print("Even Numbers:", filter_even_numbers(user_numbers))

