
def check_for_multiple(number, fizz=3, buzz=5):
    if number % fizz == 0 and number % buzz == 0:
        print("fizzbuzz")
    elif number % fizz == 0 :
        print("fizz")
    elif number % buzz == 0 :
        print("buzz")
    else:
        print(number)

def print_fizz_series(length=100):
    rng = range(1, length + 1)
    for num in rng:
        check_for_multiple(num)

print_fizz_series(100)