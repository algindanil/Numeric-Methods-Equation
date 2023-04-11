import math 

def f(x):
    return (x-3)*math.exp(3-x) - 3*x**2 - 2*x + 25

def phi(x):
    log_body = (3*x**2 + 2*x - 25) / (x-3)
    return (3 - math.log(log_body))

def simple_iteration(x_0, epsilon=1e-5):
    x_i = x_0
    i = 0
    delta_x = 1000

    print("Iteration\t\tXk\t\t|Xk-Xk-1|\t\tf(Xk)")
    
    while True:
        x_i_prev = x_i
        x_i = phi(x_i_prev)
        delta_x = x_i - x_i_prev
        i += 1
        print("{:4d}\t\t{:10.10f}\t\t{:10.10f}\t\t{:10.10f}".format(i, x_i_prev, abs(delta_x), f(x_i)))
        if (abs(delta_x) <= epsilon):
            break

if __name__ == '__main__':
    simple_iteration(0.5)