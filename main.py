from schizophrenia import Schizophrenia
from ocd import OCD
from patient import Patient
from typing import List

def main():
    List = []  # Define list

    # Create patients
    schizophrenia_patient = Schizophrenia(25, 70, 170, "Alice")
    schizophrenia_patient1 = Schizophrenia(30, 80, 180, "John")

    ocd_patient = OCD(30, 65, 165, "Adrian")

    # Read symptoms from text files
    schizophrenia_patient.symptoms("schizophrenia_symptoms.txt")
    schizophrenia_patient1.symptoms("schizophrenia_symptoms1.txt")

    # Append patients to list
    List.append(schizophrenia_patient)
    List.append(schizophrenia_patient1)

    # Sort patients by number of positive and negative symptoms
    sorted_list = sorted(List, key=lambda patient: (patient.num_positive_symptoms, patient.num_negative_symptoms),
                         reverse=True)

    # Print sorted patients
    print("Sorted patients:")
    for patient in sorted_list:
        print(f"Patient: {patient.name}")
        print(f"Diagnosis: {patient.__class__.__name__}")
        print(f"Positive symptoms: {patient.num_positive_symptoms}")
        print(f"Negative symptoms: {patient.num_negative_symptoms}")
        print("")

    # Call hospitalization method
    schizophrenia_patient.hospitalization("schizophrenia_symptoms.txt")

    if schizophrenia_patient.diagnosis == "Schizophrenia":
        print(f"{schizophrenia_patient.name} has schizophrenia")
    else:
        print(f"{schizophrenia_patient.name} does not have schizophrenia")

    schizophrenia_patient1.hospitalization("schizophrenia_symptoms1.txt")

    if schizophrenia_patient1.diagnosis == "Schizophrenia":
        print(f"{schizophrenia_patient1.name} has schizophrenia")
    else:
        print(f"{schizophrenia_patient1.name} does not have schizophrenia")

    ocd_patient.hospitalization()
    ocd_patient.symptoms("ocd_symptoms.txt")


if __name__ == '__main__':
    main()
