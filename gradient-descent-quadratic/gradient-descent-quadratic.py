def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    while steps:
        steps -= 1
        fdx = 2*a*x0 + b
        x0 = x0 - lr*fdx
    return x0
    pass