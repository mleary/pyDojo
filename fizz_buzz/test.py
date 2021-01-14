from fizz_buzz.main import check_for_multiple, print_fizz_series

assert check_for_multiple(6) == 'fizz', "Should be 'fizz'"
assert check_for_multiple(7,fizz=7) == 'fizz', "Should be 'fizz'"
assert check_for_multiple(20) == 'buzz', "Should be 'buzz'"
assert check_for_multiple(16, buzz=8) == 'buzz', "Should be 'buzz'"
