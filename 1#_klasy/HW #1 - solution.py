class Human (object):

    def __init__(self, name, age, hight,weight):
        self.name=name
        self.age=age
        self.hight=hight
        self.weight=weight

    def przedstaw_sie(self):
        return "Ja {}. Ja {} lat.".format(self.name, self.age)

    def pobierz_wiek(self):
        return self.age

    def pobierz_waga(self):
        return self.weight


class Man (Human):

    def przedstaw_sie(self):
        return "Cześć, jestem {}. Mam {} lat.".format(self.name, self.age)

    def pobierz_wiek(self):
        fake_age=self.age
        if fake_age>=10 and fake_age<=18:
            fake_age+=3
        elif fake_age>=19 and fake_age<=30:
            fake_age+=2
        elif fake_age>=31 and fake_age<=50:
            fake_age-=3
        elif fake_age>50:
            fake_age=int(fake_age+0.1*fake_age)
        return fake_age

    def pobierz_waga(self):
        fake_weight=self.weight
        if self.age<18:
            return self.weight
        if fake_weight>=80 and fake_weight<=100:
            fake_weight-=10
        elif fake_weight>100:
            fake_weight=int(fake_weight-0.1*fake_weight)
        return fake_weight


class Woman (Human):
    def przedstaw_sie(self):
        return "Heja! Na imię mam {} i mam {} lat".format(self.name, self.age)


maciek=Man('Maciek', 27, 173, 78)
slawek=Man('Sławek',55,174,110)
kuba=Man('Kuba', 8, 157, 101)
marta=Woman('Marta', 26, 170, 63)

print(maciek.przedstaw_sie())
print(maciek.pobierz_wiek())
print(maciek.pobierz_waga())

print(slawek.przedstaw_sie())
print(slawek.pobierz_wiek())
print(slawek.pobierz_waga())

print(kuba.przedstaw_sie())
print(kuba.pobierz_wiek())
print(kuba.pobierz_waga())

print(marta.przedstaw_sie())
print(marta.pobierz_wiek())
print(marta.pobierz_waga())

