class Complex():
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def get_re(self):
        return self.re

    def get_im(self):
        return self.im

    def set_re(self, re):
        self.re = re

    def module(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def add(self, other):
        self.re += other.re
        self.im += other.im

    def sum(self, other):
        new_re = self.re + other.re
        new_im = self.im + other.im
        return Complex(new_re, new_im)

    def __repr__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}j'
        if self.im == 0:
            return f'{self.re}'
        else:
            return f'{self.re} - {self.im}j'


c=Complex(3,4)
c2=Complex(5,6)
print(c.sum(c2))