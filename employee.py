
class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.company = 'evolvecyber'
        self.address = '5636 N Western Ave, Fl 1 Chicago, IL'

    @property
    def email(self):
        return '{}.{}@{}.com'.format(self.first.lower(), self.last.lower(), self.company)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
