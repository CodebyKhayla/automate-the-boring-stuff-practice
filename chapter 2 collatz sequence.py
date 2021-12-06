'''The Collatz Sequence
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that
keeps calling collatz() on that number until the function returns the value 1.  '''

def collatz(number):
    if number % 2 == 0:
        outcome = number // 2
        print(outcome)
    elif number % 2 == 1:
        outcome = 3*number+1
        print(outcome)
    return outcome

while True:
    math_magic = collatz(int(input('Enter a number ')))
    if math_magic == 1:
        break
    else:
        continue

