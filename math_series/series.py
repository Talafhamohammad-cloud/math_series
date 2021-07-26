def fibo(n):
    if n == 0:
       return n
    elif n == 1:
        return n  
    else:
       return(fibo(n-1) + fibo(n-2))
################################################################
def lucas(n) :
    a = 2
    b = 1
    if (n == 0) :
        return a
    # generating number
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
    return b
######################################################################

def sum_series(n, n1, n2):
    if type(n) != int:
        return ("Invalid Input")
    elif n < 0:
        return ("Invalid Negative Value")
    elif n == 0:
       return n1
    elif n == 1:
       return n2
    else:
       return (sum_series(n-1, n1, n2) + sum_series(n-2, n1, n2))
