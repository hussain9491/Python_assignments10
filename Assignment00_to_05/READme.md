
# Python Code Solutions

This repository contains Python solutions to various programming exercises. These exercises cover basic concepts such as functions, loops, conditionals, input/output handling, and data structures like lists and strings.

## Table of Contents

1. [Count Even Numbers](#count-even-numbers)
2. [Double the Number](#double-the-number)
3. [Get Name](#get-name)
4. [Odd or Even Numbers](#odd-or-even-numbers)
5. [Divisors of a Number](#divisors-of-a-number)
6. [Print Multiple Messages](#print-multiple-messages)
7. [Make Sentence](#make-sentence)
8. [Print Ones Digit](#print-ones-digit)
9. [Check If Adult](#check-if-adult)
10. [Greeting User](#greeting-user)
11. [In Range](#in-range)
12. [Fruit Store Inventory](#fruit-store-inventory)
13. [Get User Data](#get-user-data)
14. [Subtract Seven](#subtract-seven)

---

## 1. Count Even Numbers

### Problem:
You are given a list of numbers and you need to count how many of them are even.

### Solution:
The solution iterates through the list and uses the modulo operation to check if a number is divisible by 2 (i.e., even). If the condition is true, the count is incremented.

```python
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)
```

---

## 2. Double the Number

### Problem:
Write a function that takes a number as input and returns that number doubled.

### Solution:
The function `double()` simply multiplies the input number by 2 and returns the result. In the `main()` function, the program reads the input, calls `double()`, and prints the result.

```python
def double(num):
    return num * 2

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)
```

---

## 3. Get Name

### Problem:
Write a function that returns your name when called. In the `main()` function, it asks the user for the name and prints a greeting message.

### Solution:
The function `get_name()` returns a predefined string, which represents the user's name. In the `main()` function, the greeting message is displayed.

```python
def get_name():
    return "Sophia"

def main():
    name = get_name()
    print("Howdy", name, "! 🤠")
```

---

## 4. Odd or Even Numbers

### Problem:
Given a number, determine whether it is odd or even. Print "odd" if the number is odd, and "even" if it is even.

### Solution:
The function `is_odd()` checks whether a number is odd by calculating its remainder when divided by 2. In the `main()` function, it iterates through a range of numbers, checks if each number is odd or even, and prints the corresponding message.

```python
def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')

def is_odd(value: int):
    remainder = value % 2
    return remainder == 1
```

---

## 5. Divisors of a Number

### Problem:
Write a function that returns all divisors of a given number.

### Solution:
The function `print_divisors()` iterates through all integers up to the given number and checks if they are divisors. If the division leaves no remainder, the number is a divisor and is printed.

```python
def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)
```

---

## 6. Print Multiple Messages

### Problem:
Print a given message multiple times as specified by the user.

### Solution:
The function `print_multiple()` takes a message and a repeat count. It uses a loop to print the message the specified number of times.

```python
def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)
```

---

## 7. Make Sentence

### Problem:
Create a sentence using a word and its part of speech (noun, verb, or adjective). Based on the part of speech, print the word in a specific template.

### Solution:
The `make_sentence()` function checks the part of speech and places the word in an appropriate sentence template based on the input.

```python
def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)
```

---

## 8. Print Ones Digit

### Problem:
Extract the ones digit of a given number.

### Solution:
The function `print_ones_digit()` uses the modulo operation (`% 10`) to get the last digit of a number and print it.

```python
def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)
```

---

## 9. Check If Adult

### Problem:
Check if the given age is above or equal to the legal adult age.

### Solution:
The `is_adult()` function checks if the age is greater than or equal to the constant `ADULT_AGE` and returns a boolean value accordingly.

```python
ADULT_AGE = 18

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))
```

---

## 10. Greeting User

### Problem:
Ask the user for their name and greet them with it.

### Solution:
The program prompts the user to input their name and then greets them using that name.

```python
def main():
    name = input("What's your name? ")
    print("Greetings", name, "!")

if __name__ == "__main__":
    main()
```

---

## 11. In Range

### Problem:
Check if a given number is between two other numbers, inclusive.

### Solution:
The function `in_range()` checks if the number lies between the specified `low` and `high` values, including the boundary values.

```python
def in_range(n, low, high):
    return low <= n <= high
```

---

## 12. Fruit Store Inventory

### Problem:
Ask the user for a fruit and check if it's available in stock. If available, return the quantity; otherwise, display an out-of-stock message.

### Solution:
The `num_in_stock()` function returns the stock count for each fruit. If a fruit is not found, it returns 0, and the `main()` function handles the output message.

```python
def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    elif fruit == 'pear':
        return 1000
    else:
        return 0
```

---

## 13. Get User Data

### Problem:
Ask the user for their first name, last name, and email address, and return these pieces of data as a tuple.

### Solution:
The function `get_user_info()` collects user data and returns it as a tuple containing the first name, last name, and email.

```python
def get_user_info():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    return first_name, last_name, email_address

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)
```

---

## 14. Subtract Seven

### Problem:
Create a function that subtracts 7 from a given number.

### Solution:
The function `subtract_seven()` subtracts 7 from the input number and returns the result.

```python
def subtract_seven(num):
    return num - 7

def main():
    num = 7
    num = subtract_seven(num)
    print("This should be zero:", num)
```

---

This `README.md` file summarizes the purpose, problem, and solution for each exercise. You can refer to it for quick access to each function and its explanation.
