from dogLayla import *


dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  
dog2 = Dog("Golden Retriever", 3, 64.0, "Callypso")
dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")
dog4 = Dog("Blue Tick Hound", 4, 52.5)
dog5 = Dog("Black Laborator Retriever", 6, 73.0)


print(dog1)
print(dog3.age)

print(dog2.get_age())

print(Dog.sum_ages())

with open('dog data set.csv', newline="") as f:
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)


# Dog.instantiate_from_csv("dog data set.csv")

# print(Dog.get_dog("Pug"))

# Dog.all_dogs.sort(key=Dog.get_age, reverse=False)

# for dog in Dog.all_dogs:
    #print(dog)

working_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Working")))

print(f'Number of Working Dog breeds = {len(working_dogs)}')

toy_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Toy")))

print(f'Number of Toy Dog breeds = {len(toy_dogs)}')