#a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (___init___)
#and define a method that returns the full name of the person as a combined string.

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def printName(self):
        print(self.firstname, self.lastname)

#b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional
#argument to the constructor and define a method that prints the full name and the subject area of the student.

class Student(Person):
    def __init__(self, firstname, lastname, subject_area):
        Person.__init__(self, firstname, lastname)
        self.subject_area = subject_area
    def subjectArea(self):
        return self.subject_area
    def printNameSubject(self):
        #return "%s %s, %s" % (self.firstname, self.lastname, self.subject_area)
        print(self.firstname + ' ' + self.lastname + ', ' + self.subject_area)

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def getCourse(self):
        return self.course
    def printNameCourse(self):
        print(self.firstname + ' ' + self.lastname + ', ' + self.course)