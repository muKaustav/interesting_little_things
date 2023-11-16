import time
import random
import pandas as pd
from datetime import datetime


def fast_function(x: int, y: int) -> int:
    time.sleep(random.randint(0, 2))
    return x + y


def slower_function(x: int, y: int) -> int:
    time.sleep(random.randint(0, 5))
    return x + y


def slowest_function(x: int, y: int) -> int:
    time.sleep(random.randint(0, 10))
    return x + y


def profile(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()

        elapsed_time = (end - start).total_seconds()
        print(f"Function {func.__name__} took {elapsed_time} seconds")

        return result, elapsed_time

    return wrapper


def run_profiler(ITERATIONS):
    """
    Run the profiler for the given number of iterations, and save the results to a CSV file
    """

    results = []

    for _ in range(ITERATIONS):
        x, y = random.randint(1, 10), random.randint(1, 10)

        _, fast_time = profile(fast_function)(x, y)
        _, slower_time = profile(slower_function)(x, y)
        _, slowest_time = profile(slowest_function)(x, y)

        results.append({"Function": "fast_function", "Time": fast_time})
        results.append({"Function": "slower_function", "Time": slower_time})
        results.append({"Function": "slowest_function", "Time": slowest_time})

    df = pd.DataFrame(results)

    avg_times = (
        df.groupby("Function")["Time"]
        .mean()
        .reset_index()
        .rename(columns={"Time": "Average Time"})
    )

    avg_times.to_csv("profile.csv", index=False)


if __name__ == "__main__":
    ITERATIONS = 2  # ideally a big value to get a good average
    run_profiler(ITERATIONS)
