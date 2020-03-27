class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']

    def printMembers(self):
        print('Printing members of the harmless Birds class')
        for member in self.members:
            print('\t%s ' % member)

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animalsa
        self.members = ['Salmon', 'Trout', 'Pike']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)

class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animalsa
        self.members = ['Rabbit', 'Elephant', 'Mouse']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)