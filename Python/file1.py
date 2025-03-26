class Animals:
    name = "Animal"
    age = 0
    tail = True

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name


class Cat(Animals):
    can_meow = True

    def print_name(self):
        print("Cat", self.name)


class Dog(Animals):
    can_bark = True


pet = Animals()
pet.print_name()
pet.set_name("Tuzya")
pet.print_name()
