import math


class Printer(object):
    def __init__(self, ink_level):
        self.ink_level = ink_level

    def print(self, text):
        pages = self.calc_pages(text)

        print('Wydrukowano {} stron'.format(pages))

        self.ink_level = self.ink_level - (0.07 * pages)

    @staticmethod
    def calc_pages(text):
        return math.ceil(len(text) / 100)


printer_1 = Printer(0.3)
printer_2 = Printer(0.8)

printer_1.print('a' * 310)
printer_2.print('b' * 10000)

print(printer_1.ink_level)
print(printer_2.ink_level)