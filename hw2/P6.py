# DONE

def polynomial_eval(x, coefficients):
    n = len(coefficients)
    y = 0
    for i in range(n):
        y += coefficients[i] * x**i
    return y

def bisection_method(a, b, tolerance):
    coefficients = [-5, 1, 1]

    fa = polynomial_eval(a, coefficients)
    while abs(a - b) > tolerance:
        c = (a + b) / 2.0
        fc = polynomial_eval(c, coefficients)

        if fc == 0:
            return c 

        if fa * fc < 0:
            b = c 
        else:
            a = c 

    return (a + b) / 2.0

xa = float(input('a:'))
xb = float(input('b:'))
tol = float(input('TOL:'))

root = bisection_method(xa, xb, tol)
root_value = polynomial_eval(root, [-5, 1, 1])

print(f'f({root:.3f})={root_value:.5f}')
