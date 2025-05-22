# Day 54: ⏱️ Python Function Benchmarking with Decorators

Learn how to measure and compare the execution time of functions using a custom Python decorator! This script benchmarks a function by running it multiple times and calculating the average execution time.

## 🚀 How It Works

1. **Custom Decorator**: A parameterized decorator `@avg_runs_decorator(n)` runs a function `n` times.
2. **Timing Logic**: Each run is timed using `time.time()`, and durations are printed individually.
3. **Averaging**: After all runs, it prints the average execution time of the function.
4. **Function Testing**: Two test functions (`fast_function` and `slow_function`) are benchmarked.

## 🧠 Features

* 🛠️ Easily wraps any function to analyze performance
* 🔁 Runs multiple iterations for accuracy
* 📊 Prints per-run timing and average duration
* ⚙️ Works with any function that returns a result

## 🛠️ How to Run

1. Clone the project:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day54_FunctionTimer
   ```

2. Run the script:

   ```bash
   python main.py
   ```

## 🖥️ Example Output

```
Run 1: 0.0342s
Run 2: 0.0337s
Run 3: 0.0335s
Run 4: 0.0340s
Run 5: 0.0339s

fast_function average time over 5 runs: 0.0339s

Run 1: 0.2821s
Run 2: 0.2805s
Run 3: 0.2840s
Run 4: 0.2813s
Run 5: 0.2827s

slow_function average time over 5 runs: 0.2821s
```

## 🧪 Technologies Used

* Python 3
* `time` module for tracking performance
* Decorators for elegant code reuse

## 🎓 What I Learned

* Creating and applying parameterized decorators
* Using `*args` and `**kwargs` to support flexible functions
* Measuring and reporting function performance
* Applying timing benchmarks to performance tuning

---

💡 Great for developers who want to analyze runtime performance or compare function efficiency without third-party libraries!
