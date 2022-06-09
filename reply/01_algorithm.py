#!/usr/bin/python
# Using Leibnitz Formula 
# https://www.cuemath.com/calculus/leibniz-rule/
# with interpreter: https://replit.com/@harimau99/loopPIv1?v=1

n = int(input("Enter an integer: "))
k = 0
pi = 0
while k <= n:
# the next one line is for the formula
    ls = 4*((((-1)**k)/(2*k + 1.0)))
    pi = pi + ls
    print("%d: %.25f" %(k, pi))
    k = k + 1

# añadimos un comentario para comprensión de n_terms
n_terms = n + 1

if n == 0:
    print("The result above, is the first value of pi calculated given by user.")
else:
    print("These are the first %d values of pi calculated given by user." %(n_terms))

