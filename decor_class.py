import time


class TimeThis:
    """
    Выводит в консоль среднее время отработки функции, которую оборачивает
    параметр num_runs - количество запусков обернутой функции
    """
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __call__(self, func):
        def wrap():
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)

        return wrap


@TimeThis(num_runs=10)
def f():
    for j in range(1000000):
        pass


if __name__ == "__main__":
    f()
