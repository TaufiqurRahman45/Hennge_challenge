import sys

square_math = lambda x : x*x
sum_square_math = lambda x: x

pos_filter = lambda x: x>0

def iteration_times():
    try:
        n = int(input())
        if n <= 0 or n > 100:
            sys.stderr.write("iteration times N (1 <= N <= 100)\n")
            sys.exit(1);
    except ValueError:
        sys.stderr.write("Input integer\n")
        sys.exit(1)
    return n

def get_data():
    try:
        X = int(input())
        if X <= 0 or X > 100:
            # sys.stdin.readline() 
            raise ValueError
        Y = map(int, sys.stdin.readline().split())
    except ValueError:
        sys.stderr.write("Input Error. Try again: ")
        raise ValueError
    return Y

def calculate(times, math_func = sum_square_math, filter_func = pos_filter):
    if times == 0:
        return 0
    try:
        result = sum(map(math_func, filter(filter_func, get_data())))
        print(result)
    except ValueError:
        sys.stderr.write("at %d input dataset\n" % (times))
    return calculate(times-1, math_func, filter_func)

n = iteration_times()
calculate(n, square_math, pos_filter)