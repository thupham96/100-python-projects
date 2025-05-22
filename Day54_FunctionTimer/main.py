import time

def avg_runs_decorator(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            total_time = 0
            for i in range(n):
                start = time.time()
                result = function(*args, **kwargs)
                end = time.time()
                duration = end - start
                total_time += duration
                print(f"Run {i+1}: {duration:.4f}s")
            avg_time = total_time / n
            print(f"\n{function.__name__} average time over {n} runs: {avg_time:.4f}s\n")
            return result
        return wrapper
    return decorator

@avg_runs_decorator(5)
def fast_function():
    for i in range(1000000):
        i * i

@avg_runs_decorator(5)
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()
