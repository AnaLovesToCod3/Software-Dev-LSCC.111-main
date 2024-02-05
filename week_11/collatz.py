def collatz_steps(n):


    if n <= 0:
        raise ValueError("helo, i said positivee")

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

def find_smallest_n(x):

    if x <= 0:
        raise ValueError("again, has to be positive")

    n = 1
    while collatz_steps(n) < x:
        n += 1

    return n

if __name__ == "__main__":
    try:
        x = int(input("positive integers bitte (n): "))
        if x <= 0:
            raise ValueError("n must be positive. Try again.")

        smallest_n = find_smallest_n(x)
        print(f"The smallest n such that steps(n) >= {x} is: {smallest_n}")

    except ValueError as e:
        print(f"Error: {e}")


#i'll get back to this and make ir prettier. trust.