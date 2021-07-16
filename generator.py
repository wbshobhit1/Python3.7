"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""


def gen(n):
    for i in range(n):
        yield i


g = gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())

# print(g.__next__())  This will cause error due to stopiterator

h = 'harry'
ier = iter(h)
print(ier)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# for c in h:
#     print(c)

"""
Factorial using generators
"""

num = int(input("Enter the Number : "))


def fac(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    yield f


b = fac(num)
# print(list(b))
print(b.__next__())


"""
Fibonacci series  using generators
"""
inp = int(input("Give input:"))


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(tuple(fibo(inp)))
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
