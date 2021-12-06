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

