import Fibonacci
import time
import matplotlib.pyplot as plt
class Main:

    @staticmethod
    def main():
        # Initialize the Fibonacci instance
        fib_instance = Fibonacci.Fibonacci()

        # List of n values to calculate Fibonacci numbers for
        n_values = [501, 631, 794,1000,1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
        execution_times = []

        # List of your Fibonacci functions
        fib_functions = [fib_instance.fibonacci_3]  # Add other functions like fibonacci_2, fibonacci_3, etc.

        # Loop through each Fibonacci function
        for i, fib_func in enumerate(fib_functions, start=1):
            execution_times = []

            # Measure execution time for each term for the current function
            for n in n_values:
                exec_time = Main.measure_time(fib_func, n)
                execution_times.append(exec_time)

            # Plot the execution times
            plt.figure(figsize=(10, 6))
            plt.plot(n_values, execution_times, marker='o')
            plt.title(f'Fibonacci Function {5} Execution Time')
            plt.xlabel('n-th Fibonacci Term')
            plt.ylabel('Time (s)')
            plt.grid(True)
            plt.show()
        # Define header for the table
        print("       ", " ".join([f"{n:>7}" for n in n_values]))

        # Measure the time for each method
        for i in range(4, 5):  # Adjust range as needed for actual methods
            # For each method, print the method number and execution times for each n
            method_times = [f"{Main.measure_time(getattr(fib_instance, f'fibonacci_{i}'), n):.4f}" for n in n_values]
            print(f"Method {i}", " ".join([f"{time:>7}" for time in method_times]))
    @staticmethod
    def measure_time(function, n):
        start_time = time.perf_counter()
        function(n)
        end_time = time.perf_counter()
        return (end_time - start_time)


    # Run the main function
Main.main()