def outer(x):
    text = 'to jest tekst'

    def inner(y):
        return x ** y

    return inner


pow_of_two = outer(2)

print(pow_of_two(2))
print(pow_of_two(4))
print(pow_of_two(6))

print(outer(3)(3))