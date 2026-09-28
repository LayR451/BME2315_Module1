from dog_Tripp import *

dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  
dog2 = Dog("Golden Retriever", 3, 64.0, "Callypso")
dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")


total = 0

for dog in Dog.all_dogs:
        total += dog.age

print(total)
print(f"Total age of all dogs is: {total}")

print(Dog.sum_ages())