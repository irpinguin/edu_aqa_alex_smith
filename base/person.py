class Person():
    ''' Person model '''

    def __init__(self, name, age):
        ''' Initialization of person attributes - name, age '''
        self.name = name
        self.age = age
        print("Person was created")

    def sing(self):
        ''' ask the person to sing '''
        print(self.name + " sing")

    def dance(self):
        ''' ask the person to dance '''
        print(self.name + " dance")


man = Person("Paul", 32)
girl = Person("Girl", 18)
print(man.name)

man.sing()
girl.dance()