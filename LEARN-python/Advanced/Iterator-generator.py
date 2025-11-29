# iterator fetch item 1 by 1
# don't store the entire list in memory
# once it exhausted it cannot be reused
list=[1, 2, 3]
iterator=iter(list)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3

# generator is a special kind of iterator
# it can defined using yield
# memory efficient
# they don't store the all item instead they create them when needed
def generator():
    yield 1
    yield 2
    yield 3
gen=generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3