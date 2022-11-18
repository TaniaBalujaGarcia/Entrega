from P23_sumas import sumatorio

def sumatorioR(n):
    if n == 0:
        return 0
    else:
        return n + sumatorioR(n - 1)

def sumatorioR_function(n,f):
    if n <= 0:
        return f(0)
    else:
        return n + sumatorioR_function(n - 1, f)

print(sumatorioR(100), sumatorio(100))

print(sumatorio(1000))
# print(sumatorioR(1000))