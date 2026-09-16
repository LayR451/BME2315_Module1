# Layla Ragland's code for the class of patient 'objects'
# This code project is going to focus on the attributes of sex, education level, disease onset, age of death, length of disease, and amount of amyloid plaque.
import csv

# Defining the class as patient objects, and giving the attributes of 
# This is Part 1, and Part 2
class patient:
    all_patients = []

    def __init__(self, donor: str, sex: str, education: str, time_with_disease: float, amyloid_plaque: float, onset_age: float, death_age: float): 
        self.donor = donor
        self.sex = sex
        self.education = education
        self.onset_age = onset_age
        self.death_age = death_age
        self.time_with_disease = time_with_disease
        self.amyloid_plaque = amyloid_plaque

        patient.all_patients.append(self)

# This is Part 3, and defines what should be printed when a patient is called
    def __repr__(self):  
        return f"{self.donor}: ({self.sex} | {self.education} | {self.onset_age} | {self.death_age} | {self.time_with_disease} | {self.amyloid_plaque})"



#This class method helps for Part 5. It sorts patients based off a particular attribute using the sorted python function
# AI Usage Statement: I wrote the initial statement and then needed AI help to debug it, including the idea to add the numerous ifs to test of a value was present. 
# Because otherwise, I found that the code would error because there would be empty types appearing in the comparisons, which needed to be accomodated for.
    @classmethod
    def sort_patients(cls, attribute):
        def sort_key(patient):
            value = getattr(patient, attribute)

            # Missing values go to the bottom of print
            if value is None or value == "":
                return (1, "")

            # I am only working with floats or strings, so:
            # First, it tries to treat the value as a float
            try:
                return (0, float(value))
            except (ValueError, TypeError):
                # If it can't, it will treat it as a string
                return (0, str(value).lower())

        sorted_patients = sorted(cls.all_patients, key=sort_key)

        for patient in sorted_patients:
            print(patient)

# This method works for Part 6. For context, in this project, Tripp and I are interested in highest level education related to age of onset, and how the length that one has the disease (death - onset) related to amount of amyloid plague.
# the **criteria method means you can plug in multiple attributes and their values
    @classmethod
    def many_attributes_patients(cls, **criteria):
        for patient in cls.all_patients:
            if all(getattr(patient, attribute) == value
                for attribute, value in criteria.items()):
                print(patient)

# This is copied directly from the dog project, and is what allows me to access the whole patient dataset
    @classmethod 
    def instantiate_from_csv(cls, filename: str):

        #the code below will open the .csv file and create a list of all the rows in your spreadsheet
        
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patient_data = list(reader)
        
        #the code below will create a patient object for each row, based on the data: 
            for row in rows_of_patient_data:
                    patient(
                    donor = (row['Donor ID']),
                    sex = (row['Sex']),
                    education = (row['Highest level of education']),
                    onset_age = (row['Age of onset cognitive symptoms']),
                    death_age= (row['Age at Death']),
                    # The time with disease row needed the if statement, because without it, it throws an error if there is not a age of onset recorded. 
                    time_with_disease= (int(row['Age at Death']) - int(row['Age of onset cognitive symptoms'])) if row['Age of onset cognitive symptoms'] != '' else None,                    amyloid_plaque= (row['ABeta42 pg/ug'])
                )
                    
