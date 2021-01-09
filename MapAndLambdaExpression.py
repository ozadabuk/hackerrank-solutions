cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    if n <= 2:
        return [x for x in range(0, n)]

    f = [0, 1, 1]
    for i in range(2, n - 1):
        fib = f[-2] + f[-1]
        # print("f[-2]:" + str(f[-2]) + " + f[-1]:" + str(f[-1]) + " = " + str(fib))
        f.append(fib)
    return f
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = 2
    print(list(map(cube, fibonacci(n))))