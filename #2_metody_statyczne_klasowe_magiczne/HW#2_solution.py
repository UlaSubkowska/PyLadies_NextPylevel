# Zadanie domowe polega na dostosowaniu klasy SecretFormula (dodanie/zmiana kodu)
# w taki sposób aby program się poprawnie kompilował i printował na konsoli wyłącznie
# informację True
# Przy implementacji wykorzystaj metodę klasową/statyczną oraz dekorator (sprawdzanie poprawności hasła)
def check_password(f):
    def wrapper(self, password, *args, **kwargs):
        if self._password!=password:
            return None
        return f(self,password,*args,**kwargs)
    return wrapper


class SecretFormula(object):
    def __init__(self, secret, password=None):
        self.secret=secret
        if password is None:
            password=self.__class__._password
        self._password=password

    @classmethod
    def set_default_password(cls, default_pas):
        cls._password=default_pas

    @check_password
    def get_secret(self, password):
        return self.secret

    @check_password
    def get_password(self, password):
        return self._password

    @check_password
    def change_password(self, password, new_password):
        self._password=new_password
        return True


# Treść metody run nie ulega zmianie
def run():
    SecretFormula.set_default_password('qwerty')

    formula_default = SecretFormula(secret='Snail is a fish')
    formula_extra = SecretFormula(secret='Snake have no ears', password='12345')

    # Default formula

    password = 'not_password'
    print(formula_default.get_secret(password=password) is None)
    print(formula_default.get_password(password=password) is None)
    print(formula_default.change_password(password=password, new_password='new_password') is None)

    password = 'qwerty'
    print(formula_default.get_secret(password=password) == 'Snail is a fish')
    print(formula_default.get_password(password=password) == 'qwerty')
    print(formula_default.change_password(password=password, new_password='new_password') is True)
    print(formula_default.get_password(password='new_password') == 'new_password')

    # Extra formula

    password = 'new_password'
    print(formula_extra.get_secret(password=password) is None)
    print(formula_extra.get_password(password=password) is None)
    print(formula_extra.change_password(password=password, new_password='extra_password') is None)

    password = '12345'
    print(formula_extra.get_secret(password=password) == 'Snake have no ears')
    print(formula_extra.get_password(password=password) == '12345')
    print(formula_extra.change_password(password=password, new_password='new_password') is True)
    print(formula_extra.get_password(password='new_password') == 'new_password')

    print(formula_default._password == formula_extra._password)

run()