def is_prime(number: int):
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


def are_digits_prime(number: int):
    digits = 0
    while True:
        digit = number % 10
        number /= 10
        number = int(number)
        digits += digit
        if number == 0:
            break
    return is_prime(digits)


if __name__ == "__main__":
    i = 0
    for number in range(1000000, 10000000):
        if are_digits_prime(number) and is_prime(number):
            print(number)
            i += 1
        if i == 2:
            break
