import math 

def f(x):
    return (x-3)*math.exp(3-x) - 3*x**2 - 2*x + 25

def relaxation(x_0, epsilon=1e-5):
    x_i = x_0
    i = 0

    print("Iteration\t\tXk\t\t|Xk-Xk-1|\t\tf(Xk)")
    
    while True:
        x_i_next = x_i - 0.0216194 * f(x_i)
        delta_x = abs(x_i_next - x_i)
        if (delta_x <= epsilon):
            break
        i += 1
        print("{:4d}\t\t{:10.10f}\t\t{:10.10f}\t\t{:10.10f}".format(i, x_i, abs(delta_x), f(x_i)))
        x_i = x_i_next

if __name__ == '__main__':
    relaxation(0.5)