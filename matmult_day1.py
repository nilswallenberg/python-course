# Program to multiply two matrices using nested loops
import random
import time

N = 250

# Method 1
#@profile
def create_x(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

#@profile
def create_y(N):
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

#@profile
def create_r(N):
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

#@profile
def method_1(X,Y,result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Method 2
# Optimization
#@profile
def create_x_o(N):
    X = [[random.randint(0, 100) for i in range(N)] for j in range(N)]
    return X

#@profile
def create_y_o(N):
    Y = [[random.randint(0, 100) for i in range(N + 1)] for j in range(N)]
    return Y

#@profile
def method_2(X,Y):
    result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

# Method 3
# Numpy optimization
#@profile
def method_3(N):
    import numpy as np
    X = np.random.randint(0, 100, size=(N, N))
    Y = np.random.randint(0, 100, size=(N, N + 1))
    result = np.matmul(X, Y)
    return result

#@profile
def print_result(result):
    for r in result:
        print(r)

## Method one
start_time = time.time()

X = create_x(N)
Y = create_y(N)
result1 = create_r(N)
result1 = method_1(X,Y,result1)

time1 = time.time() - start_time

## Method two
start_time = time.time()

X_o = create_x_o(N)
Y_o = create_y_o(N)
result2 = method_2(X_o,Y_o)

time2 = time.time() - start_time

## Method three
start_time = time.time()

result3 = method_3(N)

time3 = time.time() - start_time

print((time2/time1)*100)
print((time3/time1)*100)

# For method 1 filling the results matrix takes up largest amount of time. This is to some extent fixed in method 2, where list comprehension is used instead.
# However, with numpy, speed increases a lot and instead of taking ~12-13 seconds in method 1, it now takes about 0.5 seconds.
# Method 2 takes ~50% of the time in Method 1 and Method 3 takes about ~1% of the time in Method 1.

# For memory in euler72.py most memory is taken up at line 52 and same for speed. For matmult.py most time is taken up when filling the result matrix.