class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

class people(object):
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, v):
        self._sex = v


'''u = Student()
#print(u.age)
u.birth = 2010
print(u.birth)

print(u.age)'''

p = people
p.sex = 1
print(p.sex)
print(type(p.sex))
p.sex = 'man'
print(p.sex)
print(type(p.sex))
