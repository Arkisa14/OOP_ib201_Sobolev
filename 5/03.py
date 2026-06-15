def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_password = input('Введите пароль: ')
            if user_password == password:
                return func(*args, **kwargs)
            else:
                print('В доступе отказано')
                return None
        return wrapper
    return decorator