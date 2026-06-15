def check_password(func):
    def wrapper(*args, **kwargs):
        password = input('Введите пароль: ')
        if password == 'пароль':
            return func(*args, **kwargs)
        else:
            print('В доступе отказано')
            return None
    return wrapper

@check_password
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b