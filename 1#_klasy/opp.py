class Animal(object):
    _is_alive=True

    def __init__(self, name):
        self.name=name

    def introduce(self):
        return self.name

    def kill(self):
        self._is_alive=False

    def is_dead(self):
        if self._is_alive:
            print('{} is ok'.format(self.name))
        else:
            print('{} is dead'.format(self.name))

class Mutant(Animal):
    def introduce(self):
        response=super(Mutant, self).introduce()
        response+='aaaa'

        return response

    def kill(self):
        pass

dog=Animal(name='Burek')
dog.is_dead()
dog.kill()
dog.is_dead()

cat=Animal(name='Mruczek')
cat.is_dead()
cat.kill()
cat.is_dead()

mutant=Mutant(name='Hulk')
mutant.is_dead()
mutant.kill()
mutant.is_dead()
