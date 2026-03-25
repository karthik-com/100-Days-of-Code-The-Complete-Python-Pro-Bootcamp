# Problem - FizzBuzz : print "FizzBuzz" if number divisible by 3 and 5.
		       print "Buzz" if number divisible by 5
		       print "Fuzz" if number divisible by 3

# Solution - 

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    