import time


class TimeThis:
    """
    Выводит в консоль среднее время отработки функции, которую оборачивает
    параметр num_runs - количество запусков обернутой функции
    """
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __call__(self, func):
        t0 = time.time()
        for _ in range(self.num_runs):
            func()
        t1 = time.time()
        print("Выполнение заняло %.5f секунд" % ((t1 - t0) / self.num_runs))
        return func


@TimeThis(num_runs=10)
def f():
    for j in range(1000000):
        pass


if __name__ == "__main__":
    f()
