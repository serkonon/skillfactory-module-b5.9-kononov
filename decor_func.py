import time


def time_this(num_runs=10):
    """
    Выводит в консоль среднее время отработки функции,которую оборачивает
    :param num_runs: количество запусков обернутой функции
    :return: функция-декоратор
    """
    def decorator(func):
        t0 = time.time()
        for _ in range(num_runs):
            func()
        t1 = time.time()
        print("Выполнение заняло %.5f секунд" % ((t1 - t0) / num_runs))
        return func
    return decorator


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


if __name__ == "__main__":
    f()

