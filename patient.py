import csv


class Patient:  # create a class called Patient
    all_patients = []  # create a class variable to hold all instances

    def __init__(
        self,
        donor_id: str,
        age_at_death: float,
        sex: str,
        highest_education: str,
        years_education: float,
        cognitive_status: str,
        age_onset: float,
        age_dementia_diagnosis: float,
        abeta40: float,
        abeta42: float,
        ttau: float,
        ptau: float,
    ):
        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.highest_education = highest_education
        self.years_education = years_education
        self.cognitive_status = cognitive_status
        self.age_onset = age_onset
        self.age_dementia_diagnosis = age_dementia_diagnosis
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self)

    def __repr__(self): 
        return (
            f"{self.donor_id}: ({self.sex} | {self.age_at_death} | "
            f"{self.highest_education} | {self.cognitive_status} | "
            f"ABeta42 = {self.abeta42})"
        )

    def get_age_at_death(self):
        return self.age_at_death

    @classmethod # create a class method to get patient data from a CSV file
    def instantiate_from_csv(cls, filename: str):
        with open(filename, encoding="utf8", newline="") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

        for row in rows_of_patients:
            if row["Age of onset cognitive symptoms"] != "":
                age_onset = float(row["Age of onset cognitive symptoms"])
            else:
                age_onset = None

            if row["Age of Dementia diagnosis"] != "":
                age_diagnosis = float(row["Age of Dementia diagnosis"])
            else:
                age_diagnosis = None

            if row["Years of education"] != "":
                years_education = float(row["Years of education"])
            else:
                years_education = None

            cls(
                donor_id=row["Donor ID"],
                age_at_death=float(row["Age at Death"]),
                sex=row["Sex"],
                highest_education=row["Highest level of education"],
                years_education=years_education,
                cognitive_status=row["Cognitive Status"],
                age_onset=age_onset,
                age_dementia_diagnosis=age_diagnosis,
                abeta40=float(row["ABeta40 pg/ug"]),
                abeta42=float(row["ABeta42 pg/ug"]),
                ttau=float(row["tTAU pg/ug"]),
                ptau=float(row["pTAU pg/ug"]),
            )

    @classmethod # create a class method to filter patients based on attributes
    def filter(
        cls,
        patient_list,
        sex="any",
        cognitive_status="any",
        highest_education="any",
    ):
        filtered_patients = list(patient_list)
        remove_list = []

        attr_list = (sex, cognitive_status, highest_education) 
        attr_name = ("sex", "cognitive_status", "highest_education")

        for attr in range(len(attr_list)): # iterate through each attribute
            if attr_list[attr] != "any":
                for patient in filtered_patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)

                filtered_patients = [
                    patient for patient in filtered_patients if patient not in remove_list
                ]
                remove_list.clear()

        return filtered_patients

