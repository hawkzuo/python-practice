from random import random


def numbers():
    print("Number Examples:")
    print('2+2=', 2 + 2)
    print('50-5*6=', 50 - 5 * 6)
    print('(50-5*6)/4=', (50 - 5 * 6) / 4)
    print('17 // 3=', 17 // 3)
    print('17 % 3=', 17 % 3)
    print('2 ** 7=', 2 ** 7)


def strings():
    print("\nString Examples:")
    print('doesn\'t')
    print("doesn't")
    print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
    """)
    word = 'Python'
    # [left, right) indexing
    # String are immutable
    print(word[0:2], word[2:5], word[:2] + word[2:], )
    print(word[-1], word[-2])


def lists():
    # []
    print("\nList Examples:")
    squares = [1, 4, 9, 16, 25, 36, 49]
    # Slicing
    print(squares[0], squares[-1], squares[-3:])
    # Concat
    print(squares + [64, 81, 100])
    print(squares)
    squares.append(64)
    print(squares)


def control_flows():
    print("\nControl Flows Examples:")

    x = 100 * random()
    if x < 20:
        print("Less than 20")
    elif x < 60:
        print("Less than 60")
    else:
        print("Bigger than 60")

    corpus = ['first', 'second', 'third']
    for w in corpus:
        print(w, len(w))
    #  No iterator support, make a copy before looping
    #  corpus[:]

    for i in range(5, 10):
        print(i)
    for i in range(1, 10, 3):
        print(i)
    for i in range(len(corpus)):
        print(i, "th word:", corpus[i])

    # Break statements
    # Strange Behaviors
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        # This is executed when the loop terminates through exhaustion
        # i.e. (2, n) finished
        else:
            print(n, 'is prime')
    pass


def functions():
    print("\nFunction Examples:")

    # Warning: Default argument is mutable
    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))

    # Keyword arguments
    # voltage is required, others are optional
    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")

    parrot(1000)  # 1 positional argument
    parrot(voltage=1000)  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

    # Multiple arguments
    # *arguments are of any type
    # **keywords must be of dict type
    def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])

    # Lambda functions
    def make_incrementor(n):
        return lambda x: x + n

    incrementor_42 = make_incrementor(42)
    print(incrementor_42(10))
    print(incrementor_42(20))
    print(incrementor_42(40))

    pass


def data_structures():
    # Sequences

    # Lists: can be used directly as Stacks;
    # symbol [,,...]
    list1 = [1]
    list1.append(2)
    list1.extend([3, 4, 5])
    list1.remove(4)
    list1.pop()
    print(list1)
    list1.sort()
    list1.reverse()
    print(list1)
    list2 = list1.copy()
    list1.clear()
    print(list2)

    # Queues
    # append; appendleft; pop; popleft
    from collections import deque
    queue1 = deque([3, 5, 7])
    queue1.append(10)
    queue1.appendleft(1)
    print(queue1)
    queue1.pop()
    queue1.popleft()
    print(queue1)

    # List comprehensions
    from math import pi
    print([str(round(pi, i)) for i in range(10)])

    # del statements
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    del a[2:4]  # [left, right)
    del a

    # Tuples: values separated by commas (,,,,); immutable
    # Most useful on packing/unpacking values
    v = ([1, 2, 3], [3, 2, 1])
    # mutable list inside tuples can be changed
    v[0][1] = 10
    print(v)

    # Set: hashsets;
    # symbol {,,...}
    unique_alphabets = {x for x in 'abracadabra' if x not in 'abc'}
    print(unique_alphabets)

    # Dictionary: hashtable;
    # symbol {:,:,:,...}
    squares = {x: x ** 2 for x in (2, 4, 6)}
    print(squares)
    for k, v in squares.items():
        print('key:', k, "value:", v)
    # enumerate = each_with_index
    for index, value in enumerate(['tic', 'tac', 'toe']):
        print(index, value)
    # zip = map together

    pass


def comparators():
    # in; not in
    # is; is not
    # and; or; not
    # >; <; ==
    pass


def modules():
    # Modules are *.py files
    print("BasicTutorials.modules() function")
    pass


def files():
    # File open modes:
    # 'r': read-only [default]
    # 'w': write-only
    # 'r+': read-write
    # 'a': append
    # 'b': binary-mode

    # use with is easier & shorter than try-block
    with open('data/data.json', 'r') as f:
        print(f.read())
        # f.readline() will return empty string if EOF reached
        # f.write('A new line\n') return characters written
        # f.write(b'0123456789abcdef') can also write binary

    # read json
    import json
    with open('data/data.json', 'r') as f:
        x = json.load(f)
        print(x.__class__)

    # import pickle
    # with open('data/data.json', 'rb') as f:
    #     x = pickle.load(f)
    #     print(x.__class__)

    pass


def errors():
    try:
        x = int(input("Please enter a number:"))
        print("Input number is:", x)
        raise CustomizedError("Explicitly raise error")
    except (ValueError, RuntimeError, TypeError) as e:
        print("Input is not a number")
        print(e.args)
    finally:
        print("This statement will always be executed")
    pass


class CustomizedError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
    pass



if __name__ == "__main__":
    numbers()
    strings()
    lists()
    control_flows()
    functions()
    data_structures()
    comparators()
    modules()
    # str.format()
    files()
    errors()

