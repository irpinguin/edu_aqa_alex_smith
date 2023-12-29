class Person():
    ''' Person model '''

    def __init__(self, name, age, height):
        ''' Initialization of person attributes - name, age, height, weight '''
        self.name = name
        self.age = age
        self.height = height
        self.weight = 70

    def person_description(self):
        ''' Get person's attributes '''
        description = "His/Her name is " + self.name \
                      + ", he/she is " + str(self.age) + \
                      " years old, his/her height is " + str(self.height) \
                      + " sm and weight is " + str(self.weight) + " kg"
        print(description)

    def get_weight(self):
        ''' Get person's weight '''
        print("The weight of our person: " + str(self.weight) + " kg")

    def update_weight(self, kg):
        ''' Update person's weight '''
        self.weight = kg

class Warrior(Person):
    ''' Create class warrior - child class '''

    def __init__(self, name, age, height):
        ''' Initialize attributes for parent class '''
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        ''' Get warrior's rage '''
        print("The rage of our warrior: " + str(self.rage) + " points")
    def person_description(self):
        ''' Get warrior's attributes '''
        description = self.name \
                      + ", he/she is " + str(self.age) + \
                      " years old, his/her rage charge is " + str(self.rage)
        return description

