def check_prime(array, number):
    if array[0] == number:
        return True
    else:
        step = array[0]
        for i in range(len(array) - 1, 0, -1):
            if array[i] % step == 0:
                del array[i]
    if number not in array:
        return False
    return check_prime(array[1:], number)

try:
    N = int(input("Enter a number to check if it's prime: "))
except ValueError:
    N = int(input("Invalid number, try again: "))
finally:
    if_prime = check_prime(list(range(2, N + 1)), N)
    print(if_prime)
