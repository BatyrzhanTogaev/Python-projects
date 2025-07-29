def dec(funct):
    def wrapper():
        print('До вызова')
        funct()
    return wrapper


@dec
def test():
    print('текст')


test()
