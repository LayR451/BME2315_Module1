# this will serve as the space for my new code to keep my indivdual project seperate from our final results

import statistics
from pathlib import Path
import matplotlib
from scipy import stats

matplotlib.use("macosx")
import matplotlib.pyplot as plt

from patient import Patient

# Create patient objects from the CSV file
csv_path = Path(__file__).resolve().parent / "Metadata and Protein Data for Module 1.csv"
Patient.instantiate_from_csv(str(csv_path))

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
# Disease duration = age at death - age at dementia diagnosis

disease_duration = []

for patient in Patient.all_patients:
    if patient.age_dementia_diagnosis is not None:
        duration = patient.age_at_death - patient.age_dementia_diagnosis
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

##### - Amyloid beta analysis - #####

# Extract Amyloid-Beta 40 and Amyloid-Beta 42 levels

abeta40_levels = []
abeta42_levels = []

for patient in Patient.all_patients:
    if patient.abeta40 is not None:
        abeta40_levels.append(patient.abeta40)

    if patient.abeta42 is not None:
        abeta42_levels.append(patient.abeta42)

# Print Amyloid-Beta information
print("\nAmyloid-Beta 40:")
print(f"Number of patients with Amyloid-Beta 40 data = {len(abeta40_levels)}")

if abeta40_levels:
    print(f"Mean Amyloid-Beta 40 = {statistics.mean(abeta40_levels):.2f} pg/ug")
    print(f"Standard deviation = {statistics.stdev(abeta40_levels):.2f} pg/ug")

print("\nAmyloid-Beta 42:")
print(f"Number of patients with Amyloid-Beta 42 data = {len(abeta42_levels)}")

if abeta42_levels:
    print(f"Mean Amyloid-Beta 42 = {statistics.mean(abeta42_levels):.2f} pg/ug")
    print(f"Standard deviation = {statistics.stdev(abeta42_levels):.2f} pg/ug")

# Create paired data for disease duration and Amyloid-Beta levels (chat GPT 5.6 SOL assisted)

disease_duration_abeta40 = []
abeta40_for_duration = []

disease_duration_abeta42 = []
abeta42_for_duration = []

for patient in Patient.all_patients:

    if patient.age_dementia_diagnosis is not None and patient.abeta40 is not None:
        duration = patient.age_at_death - patient.age_dementia_diagnosis
        disease_duration_abeta40.append(duration)
        abeta40_for_duration.append(patient.abeta40)

    if patient.age_dementia_diagnosis is not None and patient.abeta42 is not None:
        duration = patient.age_at_death - patient.age_dementia_diagnosis
        disease_duration_abeta42.append(duration)
        abeta42_for_duration.append(patient.abeta42)

# Linear regression and correlation for Amyloid-Beta 40

abeta40_results = stats.linregress(
    disease_duration_abeta40,
    abeta40_for_duration
)

print("\nAmyloid-Beta 40 vs Disease Duration")
print(f"Slope = {abeta40_results.slope:.4f}")
print(f"Intercept = {abeta40_results.intercept:.4f}")
print(f"r value = {abeta40_results.rvalue:.4f}")
print(f"p value = {abeta40_results.pvalue:.4f}")


# Linear regression and correlation for Amyloid-Beta 42

abeta42_results = stats.linregress(
    disease_duration_abeta42,
    abeta42_for_duration
)

print("\nAmyloid-Beta 42 vs Disease Duration")
print(f"Slope = {abeta42_results.slope:.4f}")
print(f"Intercept = {abeta42_results.intercept:.4f}")
print(f"r value = {abeta42_results.rvalue:.4f}")
print(f"p value = {abeta42_results.pvalue:.4f}")


# Create a scatter plot of disease duration vs. Amyloid-Beta 42 levels

plt.scatter(
    disease_duration_abeta42,
    abeta42_for_duration
)

plt.title("Disease Duration vs. Amyloid-Beta 42")
plt.xlabel("Disease Duration (years)")
plt.ylabel("Amyloid-Beta 42 (pg/ug)")
plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
plt.show()

"""
Output: 

Disease duration:
Number of patients with disease duration data = 36
Mean disease duration = 4.11 years
Standard deviation of disease duration = 3.87 years

Amyloid-Beta 40:
Number of patients with Amyloid-Beta 40 data = 84
Mean Amyloid-Beta 40 = 30.53 pg/ug
Standard deviation = 111.75 pg/ug

Amyloid-Beta 42:
Number of patients with Amyloid-Beta 42 data = 84
Mean Amyloid-Beta 42 = 66.98 pg/ug
Standard deviation = 160.51 pg/ug

Amyloid-Beta 40 vs Disease Duration
Slope = 19.5173
Intercept = -26.6392
r value = 0.4553
p value = 0.0053

Amyloid-Beta 42 vs Disease Duration
Slope = 9.7494
Intercept = 58.6135
r value = 0.1613
p value = 0.3473


"""