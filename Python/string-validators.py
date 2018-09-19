if __name__ == '__main__':
    alnum = alpha = digit = lower = upper = False

    for c in input():
        alnum |= c.isalnum()
        alpha |= c.isalpha()
        digit |= c.isdigit()
        lower |= c.islower()
        upper |= c.isupper()

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
