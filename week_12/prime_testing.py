def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

#so it can't be less then 2 or divisible by anything above 1 so if both are false then she's prime for sure.

def print_primes_smaller_than(n):
    primes = [num for num in range(2, n) if is_prime(num)]
    print("primes smaller than", n, "are:", primes)


try:
    user_input = int(input("enter a non-negative integer bitte: "))

    if user_input < 0:
        raise ValueError("aloo! please enter a non-negative integer")

    if is_prime(user_input):
        print(user_input, "is indeed a prime number.")
    else:
        print(user_input, "no you dummy this ain't a prime number.")

    print_primes_smaller_than(user_input)

except ValueError as e:
    print("error:", e)

except Exception as e:
    print("oop, unexpected error occurred:", e)


#onto the next one babes
