def square_elements(numbers):
    squared = list(map(lambda x: x ** 2, numbers))
    return squared

numbers = [4,5,2,9]
squared_numbers = square_elements(numbers)
print(f"The squared numbers are: {squared_numbers}")
