# Python: If-Elif-Else (Examples)

### Overview

- Most real-world situations involve making a choice between more than two options or possibilities
- For example, a movie theater may charge different ticket prices for different age groups:
  - Admission for anyone under 5 is free
  - Admission for anyone between the ages of 5 and 55 is $10.50
  - Admission for anyone older than 55 is $8.50
- In Python, you use an `if-elif-else` statement to handle such situations
- In an `if-elif-else` chain, Python checks each condition, in order, until it finds one that passes
- When a test passes, the code that follows that condition is *executed* (run), and Python skips the rest of the tests
- If both the `if` and `elif` tests fail, Python runs the code in the `else` block (essentially the default option)

### Examples
```python
# Example 1
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

---
```python
# Example 2
weather = "sunny"

if weather == "rainy":
    print("Don't forget your umbrella!")
elif weather == "snowy":
    print("Bundle up, it's cold outside!")
else:
    print("Enjoy the beautiful weather!")
```
---
```python
# Example 3
grade = "B"
score = 85

if grade == "A" or score >= 90:
    print("Excellent work!")
elif grade == "B" or score >= 80:
    print("Good job!")
else:
    print("You should review your lab notes.")
```
---
```python
# Example 4
# Determining University Year
year = int(input("Enter the year you are in at the university (1 = freshman, 2 = sophomore, 3 = junior, 4 = senior): "))

if year == 1:
    print("You are a freshman.")
elif year == 2:
    print("You are a sophomore.")
elif year == 3:
    print("You are a junior.")
elif year == 4:
    print("You are a senior.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")
```
