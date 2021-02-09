for number in range(0,16):
    print(number)
    if number % 6 == 0 or number % 10 == 0:
        print("fizzbuzz")
    elif number % 3 == 0 or number % 5 == 0:
        print("buzz")
    elif number % 2 == 0:
        print("fizz")
