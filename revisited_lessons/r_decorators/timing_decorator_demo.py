import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@timeit
def calculate_something(num):
    """
    Simple function that returns sum of all numbers up to the square of num.
    """
    total = sum(x for x in range(0, num**2))
    return total


class Calculator:
    @timeit
    def calculate_something(self, num):
        """
        an example function that returns sum of all numbers up to the square of num
        """
        total = sum(x for x in range(0, num**2))
        return total

    def __repr__(self):
        return f"calc_object:{id(self)}"


if __name__ == "__main__":
    calculate_something(10)
    calculate_something(100)
    calculate_something(1000)
    calculate_something(5000)
    calculate_something(10000)
    calc = Calculator()
    calc.calculate_something(10)
    calc.calculate_something(100)
    calc.calculate_something(1000)
    calc.calculate_something(5000)
    calc.calculate_something(10000)
