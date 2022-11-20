from datetime import datetime


def LOG(func):
    def _wrapper(*args, **kwargs):
        with open('log.csv', 'a', encoding='utf-8') as log:
            log.writelines(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M")} {func.__name__} {func.__doc__}\n')
        return func(*args, **kwargs)
    return _wrapper
