original_print = print
def print(*args):
    original_print(*[str(arg).upper() for arg in args])