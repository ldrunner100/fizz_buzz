try:
    n = range(int(raw_input("Fizz buzz counting up to ")))
except ValueError:
    print("Please only input integers.")
n = range(int(raw_input("Fizz buzz counting up to ")))
for i in n:
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
