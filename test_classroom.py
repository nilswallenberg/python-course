from classroom import Student
from classroom import Person
from classroom import Teacher


me1 = Person('Nils', 'Wallenberg')
me2 = Student('Nils', 'Wallenberg', 'Geography')
me3  =Teacher('Nils', 'Wallenberg', 'GIS')

me1.printName()
me2.printNameSubject()
me3.printNameCourse()