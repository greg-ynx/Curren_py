from src.app.CurrencyConverter.CurrencyConverter import CurrencyConverter


def main():
    print('Main')
    c = CurrencyConverter()
    t1 = c.convert('USD', 'USD', 1)
    t2 = c.convert('USD', 'EUR', 1)
    t3 = c.convert('EUR', 'USD', t2)
    if t3 == 1:
        print(True)
        print(t2, t3)
    else:
        print(t2, t3)


if __name__ == '__main__':
    main()
