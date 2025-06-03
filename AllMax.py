import math
import random

PI = 3.14141414

# Converts Fahrenheit to Centigrade
def fcentigrade(farehn):
    return (farehn - 32) * 5 / 9

# Computes the sum of digits
def sum_of_digit(num):
    return sum(int(digit) for digit in str(num))

# Reverses the digits of a number
def reverse_num(num):
    return int(str(num)[::-1])

# Sums digits of numbers in a specific range
def sum_f_and_l(num):
    return sum(sum_of_digit(i) for i in range(1, num + 1))

# Returns the maximum of two integers
def max_val(a, b):
    return max(a, b)

# Returns the minimum of two integers
def min_val(a, b):
    return min(a, b)

# Checks if a year is a leap year
def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Validates if three sides form a triangle
def valid_tri(s1, s2, s3):
    return s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1

# Checks if a number is even or odd
def is_even_odd(num):
    return 'Even' if num % 2 == 0 else 'Odd'

# Returns the name of the month given its number
def month_name(num):
    months = ["Invalid", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[num] if 1 <= num <= 12 else "Invalid"

# Checks if a character code is a number, alphabet, special character, control character, or space
def check_ch(num):
    if num.isdigit():
        return "Number"
    elif num.isalpha():
        return "Alphabet"
    elif num in ' \t\n\r\x0b\x0c':
        return "Space or Control Character"
    else:
        return "Special Character"

# Validates if three angles form a triangle
def valid_triangle(angle1, angle2, angle3):
    return angle1 + angle2 + angle3 == 180

# Calculates the area of a circle given its radius
def circle_area(radius):
    return PI * radius * radius

# Computes the factorial of a number
def fact(num):
    return math.factorial(num)

# Prints Fibonacci numbers up to a specified value
def fib_fun(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Checks if a number is an Armstrong number
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(digit) ** power for digit in digits)

# Evaluates a mathematical expression
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        return str(e)

# Converts a decimal number to binary
def bin_val(dec):
    return bin(dec)[2:]

# Converts a binary number to decimal
def dec_val(bin_num):
    return int(str(bin_num), 2)

# Prints various patterns based on input
def patterns(n):
    for i in range(n):
        print('*' * (i + 1))
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Prints Pythagorean triples up to a specified value
def pytha(n):
    for a in range(1, n):
        for b in range(a, n):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and c <= n:
                print(f"{a} {b} {int(c)}")

# Prints Pascal's triangle up to a specified row
def pascal(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(math.comb(i, j), end=' ')
        print()

# Computes the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Computes the least common multiple (LCM) of two numbers using a conventional method
def lcm_conventional(a, b):
    return a * b // gcd(a, b)

# Computes the least common multiple (LCM) of two numbers using GCD
def lcm(a, b):
    return a * b // gcd(a, b)

# Checks if a number is a perfect number
def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

# Checks if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Prints an empty diamond shape
def print_empty_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))

# Prints a pyramid of alphabets
def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + ''.join(chr(65 + j) for j in range(i + 1)))

# Counts the occurrences of digits in a number
def count_digits(num):
    counts = [0] * 10
    for digit in str(num):
        counts[int(digit)] += 1
    for i in range(10):
        if counts[i] > 0:
            print(f"Digit {i}: {counts[i]} times")

# Prints a special pattern with characters
def special_pat(n):
    for i in range(n):
        print(''.join(chr(65 + (i + j) % 26) for j in range(i + 1)))

# Prints a pattern with decreasing numbers in a square matrix
def pattern_4321_sq(rows):
    for i in range(rows):
        print(' '.join(str(rows - j) for j in range(rows)))

# Array operations
def display(array):
    print(' '.join(map(str, array)))

def assign_random_values(array):
    for i in range(len(array)):
        array[i] = random.randint(0, 100)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def find_max(array):
    return max(array)

def find_second_largest(array):
    first, second = float('-inf'), float('-inf')
    for num in array:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

def find_index_of_max(array):
    return array.index(max(array))

def search_number(array, num):
    return array.index(num) if num in array else -1

def sum_of_array(array):
    return sum(array)

def sum_of_odd_numbers(array):
    return sum(num for num in array if num % 2 != 0)

def sum_of_even_indexes(array):
    return sum(array[i] for i in range(0, len(array), 2))

def is_palindrome_array(array):
    return array == array[::-1]

def find_common_numbers(array1, array2):
    common = set(array1) & set(array2)
    print(f"Common numbers: {common}")

def find_different_numbers(array1, array2):
    different = set(array1) ^ set(array2)
    print(f"Different numbers: {different}")

def count_occurrences(array):
    from collections import Counter
    occurrences = Counter(array)
    for num, count in occurrences.items():
        print(f"Number {num}: {count} times")

def find_max_occurrences(array):
    from collections import Counter
    occurrences = Counter(array)
    max_occurrence = max(occurrences.values())
    max_occurrences = [num for num, count in occurrences.items() if count == max_occurrence]
    return max_occurrences

def find_least_occurrences(array):
    from collections import Counter
    occurrences = Counter(array)
    min_occurrence = min(occurrences.values())
    least_occurrences = [num for num, count in occurrences.items() if count == min_occurrence]
    return least_occurrences

def display_string_list(string_list):
    print(" ".join(string_list))

def sort_string_list(string_list):
    string_list.sort()
    display_string_list(string_list)

def search_string_in_list(string_list, target):
    if target in string_list:
        print(f"String '{target}' found at index {string_list.index(target)}")
    else:
        print(f"String '{target}' not found")

# Main function to demonstrate functionality
if __name__ == "__main__":
    print(f"Fahrenheit to Centigrade: {fcentigrade(32)}")
    print(f"Sum of digits of 1234: {sum_of_digit(1234)}")
    print(f"Reverse of 1234: {reverse_num(1234)}")
    print(f"Sum of digits from 1 to 10: {sum_f_and_l(10)}")
    print(f"Max of 5 and 10: {max_val(5, 10)}")
    print(f"Min of 5 and 10: {min_val(5, 10)}")
    print(f"Leap year check for 2024: {leap(2024)}")
    print(f"Valid triangle with sides 3, 4, 5: {valid_tri(3, 4, 5)}")
    print(f"Is 4 even or odd: {is_even_odd(4)}")
    print(f"Month name for 5: {month_name(5)}")
    print(f"Character 'A' check: {check_ch('A')}")
    print(f"Valid triangle with angles 60, 60, 60: {valid_triangle(60, 60, 60)}")
    print(f"Area of circle with radius 5: {circle_area(5)}")
    print(f"Factorial of 5: {fact(5)}")
    print("Fibonacci numbers up to 50:")
    fib_fun(50)
    print(f"Is 153 an Armstrong number: {is_armstrong(153)}")
    print(f"Expression evaluation for '2 + 2 * 2': {evaluate_expression('2 + 2 * 2')}")
    print(f"Decimal 10 to binary: {bin_val(10)}")
    print(f"Binary '1010' to decimal: {dec_val('1010')}")
    print("Pattern:")
    patterns(5)
    print("Pythagorean triples up to 20:")
    pytha(20)
    print("Pascal's triangle with 5 rows:")
    pascal(5)
    print(f"GCD of 56 and 98: {gcd(56, 98)}")
    print(f"LCM of 4 and 6: {lcm(4, 6)}")
    print(f"Is 28 a perfect number: {is_perfect(28)}")
    print(f"Is 12321 a palindrome: {is_palindrome(12321)}")
    print("Empty diamond pattern with 5 rows:")
    print_empty_diamond(5)
    print("Alphabet pyramid with 5 rows:")
    print_pyramid(5)
    print("Digit counts in 112233:")
    count_digits(112233)
    print("Special pattern with 5 rows:")
    special_pat(5)
    print("Pattern 4321 square with 4 rows:")
    pattern_4321_sq(4)

    # Array operations example
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Array:", arr)
    print("Array sorted with insertion sort:")
    insertion_sort(arr)
    display(arr)
    print("Array sorted with selection sort:")
    selection_sort(arr)
    display(arr)
    print("Array sorted with bubble sort:")
    bubble_sort(arr)
    display(arr)
    print(f"Max value in array: {find_max(arr)}")
    print(f"Second largest value in array: {find_second_largest(arr)}")
    print(f"Index of max value in array: {find_index_of_max(arr)}")
    print(f"Index of 50 in array: {search_number(arr, 50)}")
    print(f"Sum of array values: {sum_of_array(arr)}")
    print(f"Sum of odd numbers in array: {sum_of_odd_numbers(arr)}")
    print(f"Sum of even indexes in array: {sum_of_even_indexes(arr)}")
    print(f"Is array palindrome: {is_palindrome_array(arr)}")
    arr2 = [random.randint(0, 100) for _ in range(10)]
    print("Array 2:", arr2)
    find_common_numbers(arr, arr2)
    find_different_numbers(arr, arr2)
    count_occurrences(arr)
    print(f"Most frequent occurrences: {find_max_occurrences(arr)}")
    print(f"Least frequent occurrences: {find_least_occurrences(arr)}")

    # String operations example
    str_list = ["banana", "apple", "cherry"]
    print("String list:", str_list)
    sort_string_list(str_list)
    search_string_in_list(str_list, "apple")
