import math 

def f(x):
    return (x-3)*math.exp(3-x) - 3*x**2 - 2*x + 25

def df(x):
    return math.exp(3-x)*(4-x)- 6*x - 2

def modified_newton(x0, epsilon=1e-5):
    x_i = x0
    i = 0

    print("Iteration\t\tXk\t\t|Xk-Xk-1|\t\tf(Xk)")

    while True:
        x_i_next = x_i - (f(x_i) / df(x_i))
        delta_x = abs(x_i_next - x_i)
        i += 1
        print("{:4d}\t\t{:10.10f}\t\t{:10.10f}\t\t{:10.10f}".format(i, x_i, abs(delta_x), f(x_i)))
        if (delta_x <= epsilon):
            break
        x_i = x_i_next

if __name__ == '__main__':
    modified_newton(0.5)