from models import Animal, Dog, Cat

def main():
    dog1 = Dog("Rex", 5, "Brown", "Labrador")
    cat1 = Cat("Mimi", 3, "White", True)
    animal1 = Animal("Generic", 2, "Gray")

    animals = [dog1, cat1, animal1]

  
    for animal in animals:
        print(animal)             
        print(animal.info())     
        print(animal.speak())  
        print("-" * 30)

    
    print(dog1.fetch())
    print(cat1.scratch())


if __name__ == "__main__":
    main()