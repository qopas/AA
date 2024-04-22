from decimal import Decimal, getcontext

class Fibonacci:



    # Iterative Fibonacci
    def fibonacci_1(self,n):
        assert n >= 0
        previous_fib = 0
        current_fib = 1
        if(n==0):
            return previous_fib
        if(n==1):
            return current_fib
        else:
            for i in range(1,n):
                next_fib = current_fib + previous_fib
                previous_fib = current_fib
                current_fib = next_fib
            return current_fib


    # Recursive Fibonacci
    def fibonacci_2(self,n):
        assert n >= 0
        if(n==0):
            return 0
        if(n==1):
            return 1
        else:
            return self.fibonacci_2(n-1) + self.fibonacci_2(n-2)


    # Dynamic Programming Fibonacci
    def fibonacci_3(self,n):
        assert n >= 0
        fib = [0,1]
        for i in range(2,n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]


    # Matrix Exponentiation Fibonacci
    def fibonacci_4(self,n):
        # nested functions
        def multiply_matrices(a, b):
            return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                    [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

        def power_matrix(matrix, power):
            if power == 1:
                return matrix
            if power % 2 == 0:
                half_power = power_matrix(matrix, power // 2)
                return multiply_matrices(half_power, half_power)
            else:
                return multiply_matrices(matrix, power_matrix(matrix, power - 1))

        if n == 0:
            return 0
        if n == 1:
            return 1
        fibonacci_matrix = [[1, 1], [1, 0]]
        result_matrix = power_matrix(fibonacci_matrix, n - 1)
        return result_matrix[0][0]  # This will give F_n


    # Binet's Formula Fibonacci
    def fibonacci_5(self, n):
        assert n >= 0
        getcontext().prec = 50
        sqrt_5 = Decimal(5).sqrt()
        phi = (1 + sqrt_5) / 2
        psi = (1 - sqrt_5) / 2
        return (phi ** n - psi ** n) / sqrt_5


    # Fast Doubling Fibonacci
    def fibonacci_6(self,n):
        # nested functions
        def fast_doubling(n):
            if n == 0:
                return (0, 1)
            else:
                a, b = fast_doubling(n // 2)
                c = a * ((b << 1) - a)
                d = a * a + b * b
                if n & 1:
                    return (d, c + d)
                else:
                    return (c, d)

        return fast_doubling(n)[0]