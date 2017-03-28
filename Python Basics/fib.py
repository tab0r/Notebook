fib = [0, 1]

def fibonacci(n):
    if n in [0, 1]:
        return fib[n]
    else:
        for i in range(2, n):
            print(fib[i-1] + fib[i-2])
            fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

print(fibonacci(70))
