import time


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time}")
        return result

    return wrapper


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
        print(f"Функция вызвана с параметрами:\n{args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """

    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'count'):
            wrapper.count = 0
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"Функция была вызвана: {wrapper.count} раз")
        return result

    return wrapper


def memo(func):
  """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
  cache = {}

  def fmemo(*args):
    if args in cache:
        return cache[args]
    result = func(*args)
    cache[args] = result
    return result

  fmemo.cache = cache
  return fmemo