# anonymous function, which filters odd numbers from the given list of numbers
# using filter function and applies the square operation on each odd number
# using the map function
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

nums_filtered = map(lambda x: x * x, filter(lambda x: x % 2, nums))

print("*** Usage of an anonymous function ***")
print(list(nums_filtered))
print("---------------------------------------------------------------")


# Higher-order function trace for tracing the intermediate steps
# of the recursive function exp(x, n)
def trace(f):
    f.indent = 0

    def g(x, y):
        print('|  ' * f.indent + '|--', f.__name__, x, ',', y)
        f.indent += 1
        value = f(x, y)
        print('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value

    return g


# recursive function exp(x, n) which calculates x to the power of n
@trace
def exp(x, n):
    """
    Computes the result of x raised to the power of n.
    """
    if n == 0:
        return 1
    else:
        return x * exp(x, n - 1)


print("*** Usage of a higher-order function ***")
print(exp(4, 3))
print("---------------------------------------------------------------")
