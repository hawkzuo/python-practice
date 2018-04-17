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
                print(n, 'equals', x, '*', n//x)
                break
        # This is executed when the loop terminates through exhaustion
        # i.e. (2, n) finished
        else:
                print(n, 'is prime')
    pass


def functions():
    print("\nFunction Examples:")

    pass


if __name__ == "__main__":
    numbers()
    strings()
    lists()
    control_flows()
    functions()
