'''
Sources used to complete this assignment include pythontutorial.net for basic syntax assistance, and ChatGPT 5.6 Luna for
additional understanding with syntax, specifically for graph creation. ChatGPT 5.6 Luna also assisted in the troubleshoot process when graphs were not displaying properly and to
help with graph customization including the title, xlabel, and ylabel. I used the matplotlib online webpaage to understand the library and its functions. 
The internal VS code AI assistant was used to assist with fixing errors associated with code indentation. 

For this assignment I decided to look at the relationship between years of education and age of onset of cognitive symptoms. I also looked at the relationship between highest 
level of education and disease duration. I used a bar graph to display the mean disease duration for each level of education, with error bars representing the standard deviation. 
I used a scatter plot to display the relationship between years of education and age of onset of cognitive symptoms.
'''


import statistics
from pathlib import Path
import matplotlib
from scipy import stats
import numpy as np
import statistics 
import pandas as pd 
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


matplotlib.use("macosx")  # Use the macOS backend for matplotlib
import matplotlib.pyplot as plt

from patient import Patient

# Create patient objects from the CSV file
csv_path = Path(__file__).resolve().parent / "Metadata and Protein Data for Module 1.csv"
Patient.instantiate_from_csv(str(csv_path))

# Remove identified outlier patient
Patient.all_patients = [
    p for p in Patient.all_patients
    if p.donor_id != "H20.33.018"
]

# Check how many patients were created
print(f"Number of patients = {len(Patient.all_patients)}")

# Sort patients by age at death
Patient.all_patients.sort(key=Patient.get_age_at_death, reverse=False)

print("\nPatients sorted by age at death:")
for patient in Patient.all_patients:
    print(patient)

# Filter patients using two attributes
# Female patients with dementia
female_dementia_patients = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia",
)

print("\nFemale patients with dementia:")
for patient in female_dementia_patients:
    print(patient)

print(f"Number of female patients with dementia = {len(female_dementia_patients)}")

# Calculate disease duration
# Disease duration = age at death - age of symptom onset

disease_duration = []

for patient in Patient.all_patients:
    if patient.age_onset is not None:
        duration = patient.age_at_death - patient.age_onset
        disease_duration.append(duration)

# Print disease duration information
print("\nDisease duration:")
print(f"Number of patients with disease duration data = {len(disease_duration)}")
if disease_duration:
    print(f"Mean disease duration = {statistics.mean(disease_duration):.2f} years")
    print(f"Standard deviation of disease duration = {statistics.stdev(disease_duration):.2f} years")
else:
    print("Mean disease duration = N/A")
    print("Standard deviation of disease duration = N/A")

# Bar graph
# Mean disease duration +/- standard deviation for each education level
high_school_duration = []
trade_school_duration = []
bachelors_duration = []
graduate_duration = []
professional_duration = []

for patient in Patient.all_patients:
    if patient.age_onset is not None:
        duration = patient.age_at_death - patient.age_onset

        if patient.highest_education == "High School":
            high_school_duration.append(duration)
        elif patient.highest_education == "Trade School/ Tech School":
            trade_school_duration.append(duration)
        elif patient.highest_education == "Bachelors":
            bachelors_duration.append(duration)
        elif patient.highest_education == "Graduate (PhD/Masters)":
            graduate_duration.append(duration)
        elif patient.highest_education == "Professional":
            professional_duration.append(duration)


def safe_mean(values):
    return statistics.mean(values) if values else 0.0


def safe_stdev(values):
    return statistics.stdev(values) if len(values) > 1 else 0.0

# Calculate means
mean_high_school = safe_mean(high_school_duration)
mean_trade_school = safe_mean(trade_school_duration)
mean_bachelors = safe_mean(bachelors_duration)
mean_graduate = safe_mean(graduate_duration)
mean_professional = safe_mean(professional_duration)

# Calculate standard deviations
stdev_high_school = safe_stdev(high_school_duration)
stdev_trade_school = safe_stdev(trade_school_duration)
stdev_bachelors = safe_stdev(bachelors_duration)
stdev_graduate = safe_stdev(graduate_duration)
stdev_professional = safe_stdev(professional_duration)

# Print statistics
print("\nDisease duration by education level:")
print(f"High School: mean = {mean_high_school:.2f}, SD = {stdev_high_school:.2f}")
print(f"Trade School: mean = {mean_trade_school:.2f}, SD = {stdev_trade_school:.2f}")
print(f"Bachelors: mean = {mean_bachelors:.2f}, SD = {stdev_bachelors:.2f}")
print(f"Graduate: mean = {mean_graduate:.2f}, SD = {stdev_graduate:.2f}")
print(f"Professional: mean = {mean_professional:.2f}, SD = {stdev_professional:.2f}")

# Make bar graph

education_labels = [
    "High School",
    "Trade School",
    "Bachelors",
    "Graduate",
    "Professional",
]

education_means = [
    mean_high_school,
    mean_trade_school,
    mean_bachelors,
    mean_graduate,
    mean_professional,
]

education_stdev = [
    stdev_high_school,
    stdev_trade_school,
    stdev_bachelors,
    stdev_graduate,
    stdev_professional,
]

# Labels to make the bar graph more readable


plt.bar(
    education_labels,
    education_means,
    yerr=education_stdev,
    capsize=5
)

plt.title(
    "Mean Disease Duration by Highest Education Level"
)

plt.xlabel(
    "Highest Education Level"
)

plt.ylabel(
    "Mean Disease Duration (years)"
)

plt.xticks(rotation=20)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
plt.show()

# Scatter plot
# Years of education vs. age of onset of cognitive symptoms

years_education = []
age_onset = []

for patient in Patient.all_patients:
    if patient.age_onset is not None and patient.years_education is not None:
        years_education.append(patient.years_education)
        age_onset.append(patient.age_onset)


model = linear_model.LinearRegression()
model.fit(np.array(years_education).reshape(-1, 1), np.array(age_onset).reshape(-1, 1))

X = np.linspace(
    min(years_education),
    max(years_education),
    100
).reshape(-1, 1)

# Calculate p-value
slope, intercept, r_value, p_value, standard_error = stats.linregress(
    years_education,
    age_onset
)

# Make scatter plot
plt.scatter(
    years_education,
    age_onset
)

plt.title(
    "Years of Education vs. Age of Onset of Cognitive Symptoms"
)

plt.xlabel(
    "Years of Education (years)"
)

plt.ylabel(
    "Age of Onset of Cognitive Symptoms (years)"
)

plt.grid(
    linestyle="--",
    alpha=0.5
)
# Add regression line
plt.plot(X, model.predict(X).ravel(), color="red", linewidth=2)

plt.tight_layout()
plt.show()

# make r squared value
r_squared = model.score(np.array(years_education).reshape(-1, 1), np.array(age_onset).reshape(-1, 1))
print(f"R-squared value: {r_squared:.2f}")
print(f"P-value: {p_value:.3f}")