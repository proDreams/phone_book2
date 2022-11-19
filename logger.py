from datetime import datetime


def LOG(func):
    def wrapper(*args):
        func(*args)
        with open('log.csv', 'a', encoding='utf-8') as log:
            log.writelines(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M")} {func.__name__}\n')
    return wrapper
