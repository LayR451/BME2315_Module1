# This is Layla Ragland's main for the patient demo project

# To begin, I'm calling the patient file in so I can access those functions
from patient_Layla import *

patient.instantiate_from_csv("Metadata and Protein Data for Module 1.csv")


#Now, I will create patient objects:
# This is Part 4
patient1 = patient('Person_01', 'Female', 'High School', 20.0, 72.06, 55, 75)

patient2 = patient('Person_02', 'Male', 'Graduate (PhD/Masters)', 10, 1, 70, 80)

patient3 = patient('Person_03', 'Female', 'Bachelors', 16.0, 30, 76, 90)



# Here, I want to show my Class Method that allows me to call patients with a certian thing:
# For numerical things, it sorts them from low to high, for qualitative things, it prints alphabetically

# uncomment below to try different types:
# patient.sort_patients("amyloid_plaque")
# patient.sort_patients('onset_age')
# patient.sort_patients('sex') 



# This is the completition of part 6. The method prints the patients who are both of the criteria given:

#Uncomment below to try it:
# I decided to make attributes for matching
patient.many_attributes_patients(education = 'High School', sex = 'Female' )
patient.many_attributes_patients(amyloid_plaque = 20, age_of_death = 80 )


