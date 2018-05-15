import math


class Printer(object):
    ink_consumption = 0.07

    def __init__(self, ink_level):
        self.ink_level = ink_level

    def print(self, text):
        pages = self.calc_pages(text)

        print('Wydrukowano {} stron'.format(pages))

        self.ink_level = self.ink_level - (self.ink_consumption * pages)

    @staticmethod
    def calc_pages(text):
        return math.ceil(len(text) / 100)

    @classmethod
    def get_type(cls):
        return 'My type is {}'.format(
            cls.__name__
        )


class ColorPrinter(Printer):
    ink_consumption = 0.05


class MagicPrinter(Printer):
    ink_consumption = -0.01

    def __call__(self):
        self.ink_level = 0

    def __str__(self):
        return self.get_type()


printer_1 = Printer(0.3)
# printer_2 = ColorPrinter(0.8)

# printer_1.print('a' * 310)
# printer_2.print('b' * 10000)

# print(printer_1.get_type())