# This is Layla Ragland's main for the patient demo project

# To begin, I'm calling the patient file in so I can access those functions
from patient_Layla import *

# these other functions will help with the math and plotting skills needed from graphs
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics


# reading out of the csv file
patient.instantiate_from_csv("Metadata and Protein Data for Module 1.csv")


#Now, I will create patient objects:
# This is Part 4
patient1 = patient('Person_01', 'Female', 'High School', 20.0, 72.06, 55, 75)

patient2 = patient('Person_02', 'Male', 'Graduate (PhD/Masters)', 10, 1, 70, 80)

patient3 = patient('Person_03', 'Female', 'Bachelors', 16.0, 30, 76, 90)



# This is part 5, my Class Method that allows me to call patients with a certian thing:
# For numerical things, it sorts them from low to high, for qualitative things, it prints alphabetically
#
# uncomment below to try different types:
# patient.sort_patients("amyloid_plaque")
# patient.sort_patients('onset_age')
# patient.sort_patients('sex') 



# This is the completition of part 6. The method prints the patients who are both of the criteria given:
#Uncomment below to try it:
# This part was sooooooo hard for me. It took way too long, I kept throwing errors that I don't know how I made them- but we did it.
# patient.filter(education = 'High School', sex = 'Female' )
# patient.filter(amyloid_plaque_min = 20, death_age_max = 80 )


# The following code is edited from the dog file
# This is Part 7 and 8 
# By the way, these plots do take some time to run. :)

# Bar Graph First! This is male and female in relation to amyloid plaque

# list to put data in
amyloid_Male = []
amyloid_Female = []

# filter feature to fill the list with the desired data points
for p in patient.filter(sex="Male"):
    amyloid_Male.append(float(p.amyloid_plaque))
for p in patient.filter(sex="Female"):
    amyloid_Female.append(float(p.amyloid_plaque))

# finding means for bar graph
x_Male_bar = statistics.mean(amyloid_Male)
x_Female_bar = statistics.mean(amyloid_Female)

# Standard deviation will create the range bars
amyloid_Male_stdev = statistics.stdev(amyloid_Male)
amyloid_Female_stdev = statistics.stdev(amyloid_Female)

# Label creation!
print(f'x_Male_bar = {x_Male_bar}, amyloid_Male_stdev = {amyloid_Male_stdev}')
print(f'x_Female_bar = {x_Female_bar}, amyloid_Female_stdev = {amyloid_Female_stdev}')

sex_cols = ['Male', 'Female']
mean_sex = [x_Male_bar, x_Female_bar]
stdev_sex = [amyloid_Male_stdev, amyloid_Female_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]


# Plot and show
plt.bar(sex_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Amyloid Plaque Levels by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Amyloid Plaque (pg/µg)")
plt.show()


# Now for the scatterplot! This is length of time that disease was had (from onset to death) related to the amount of amyloid plaque

# same thing, empty lists 
disease_length = []
amyloid_plaque_levels = []

# adding data to lists
for p in patient.all_patients:
    disease_length.append(p.time_with_disease)

for p in patient.all_patients:
    amyloid_plaque_levels.append(p.amyloid_plaque)


X = [disease_length]        # Independent variable goes on x
y = [amyloid_plaque_levels] # Dependent variable goes on y 

# Plot and show
plt.scatter(X, y, color='blue')
plt.xlabel('Length of Disease (years)')
plt.ylabel('Amyloid Plaque (pg/µg)')
plt.title('Scatter Plot of Disease Length vs Amyloid Plaque')
plt.show()

#Yay! 